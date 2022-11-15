from __future__ import annotations

from typing import Type, Union

import pydantic
import pydantic.generics
from pydantic.fields import SHAPE_DICT
from pydantic.typing import (
    get_args,
    is_union,
    get_origin,
    is_none_type,
    is_literal_type,
)

from ._types import Query, ModelT, Headers, Timeout, NotGiven, RequestFiles
from ._utils import is_list, is_mapping

__all__ = ["BaseModel", "GenericModel"]


class BaseModel(pydantic.BaseModel):
    # Override the 'construct' method in a way that supports recursive parsing without validation.
    # Based on https://github.com/samuelcolvin/pydantic/issues/1168#issuecomment-817742836.
    @classmethod
    def construct(cls: Type[ModelT], _fields_set: set[str] | None = None, **values: object) -> ModelT:
        m = cls.__new__(cls)
        fields_values: dict[str, object] = {}

        config = cls.__config__

        for name, field in cls.__fields__.items():
            key = field.alias
            if key not in values and config.allow_population_by_field_name:
                key = name

            if key in values:
                value = values[key]
                if value is None:
                    fields_values[name] = field.get_default()
                else:
                    # we need to use the origin class for any types that are subscripted generics
                    # e.g. Dict[str, object]
                    origin = get_origin(field.type_) or field.type_

                    # We currently do not support field types such as `Dict[str, MyModel]`
                    if field.shape == SHAPE_DICT:
                        if issubclass(origin, BaseModel) or issubclass(origin, GenericModel):
                            raise RuntimeError(
                                f"Dictionary fields with nested models aren't supported yet; Encountered type: {field.type_}"
                            )

                    # We currently do not support constructing unions of types, e.g. `bool | MyModel` or `MyModel | MyOtherModel`
                    # But we stil have to support `Optional[T]` which is shorthand for `Union[T, None]`
                    if is_union(origin):
                        args = get_args(field.type_)
                        none_index = next((i for i, x in enumerate(args) if is_none_type(x)), None)
                        if none_index is None or len(args) > 2:
                            raise RuntimeError(f"Unsupported union type: {field.type_}")

                        # Use the non None type for the rest of our construction.
                        #
                        # Note that if the `value` was None then we wouldn't reach this code path
                        # but this raw type may be inaccurate for `list` types as it points to the items type,
                        # e.g. the `T` in `list[T]`
                        if none_index == 1:
                            raw_type = args[0]
                        else:
                            raw_type = args[1]
                    else:
                        raw_type = field.type_

                    # Recalculate the `origin` based off of the potentially new `raw_type` that has been found
                    origin = get_origin(raw_type) or raw_type

                    if not is_literal_type(raw_type) and (
                        issubclass(origin, BaseModel) or issubclass(origin, GenericModel)
                    ):
                        if is_list(value):
                            fields_values[name] = [
                                raw_type.construct(**entry) if is_mapping(entry) else entry for entry in value
                            ]
                        elif is_mapping(value):
                            fields_values[name] = field.outer_type_.construct(**value)
                        else:
                            fields_values[name] = value
                    else:
                        fields_values[name] = value
            elif not field.required:
                fields_values[name] = field.get_default()

        for key, value in values.items():
            if key not in cls.__fields__:
                # TODO: add support for constructing nested unknown models
                fields_values[key] = value

        object.__setattr__(m, "__dict__", fields_values)
        if _fields_set is None:
            _fields_set = set(fields_values.keys())
        object.__setattr__(m, "__fields_set__", _fields_set)
        m._init_private_attributes()
        return m


class GenericModel(BaseModel, pydantic.generics.GenericModel):
    pass


class FinalRequestOptions(pydantic.BaseModel):
    method: str
    url: str
    params: Query = {}
    headers: Union[Headers, NotGiven] = NotGiven()
    max_retries: Union[int, NotGiven] = NotGiven()
    timeout: Union[float, Timeout, None, NotGiven] = NotGiven()
    files: Union[RequestFiles, None] = None
    idempotency_key: Union[str, None] = None

    # It should be noted that we cannot use `json` here as that would override
    # a BaseModel method in an incompatible fashion.
    json_data: Union[Query, None] = None
    extra_json: Union[Query, None] = None

    class Config(pydantic.BaseConfig):
        arbitrary_types_allowed: bool = True

    def get_max_retries(self, max_retries: int) -> int:
        if isinstance(self.max_retries, NotGiven):
            return max_retries
        return self.max_retries
