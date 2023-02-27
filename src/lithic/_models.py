from __future__ import annotations

from typing import Any, Type, Union, cast
from typing_extensions import final

import pydantic
import pydantic.generics
from pydantic.fields import ModelField
from pydantic.typing import (
    get_args,
    is_union,
    get_origin,
    is_none_type,
    is_literal_type,
)

from ._types import (
    Body,
    Query,
    ModelT,
    Headers,
    Timeout,
    NotGiven,
    AnyMapping,
    RequestFiles,
)
from ._utils import is_list, is_mapping, strip_not_given

__all__ = ["BaseModel", "GenericModel"]


class BaseModel(pydantic.BaseModel):
    def __str__(self) -> str:
        return f'{self.__repr_name__()}({self.__repr_str__(", ")})'

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
                fields_values[name] = _construct_field(value=value, field=field)
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


def _construct_field(value: object, field: ModelField) -> object:
    if value is None:
        return field.get_default()

    origin = get_origin(field.type_) or field.type_

    if is_union(origin):
        return _construct_union_field(value=value, field=field)

    return _construct_type(value=value, type_=field.type_, outer_type=field.outer_type_)


def _construct_union_field(value: object, field: ModelField) -> object:
    args = get_args(field.type_)
    none_index = next((i for i, x in enumerate(args) if is_none_type(x)), None)
    if none_index is None or len(args) > 2:
        # try validating all variants in strict mode first to get more accurate deserialization
        new_value, error = field.validate(value, {}, loc=field.name)
        if not error:
            return new_value

        # if the data is not valid, use the first variant that doesn't fail while deserializing
        for variant in args:
            try:
                return _construct_type(value=value, type_=variant, outer_type=variant)
            except Exception:
                continue

        raise RuntimeError(f"Could not convert data into a valid instance of {field.type_}")

    # Use the non None type for the rest of our construction.
    #
    # Note that if the `value` was None then we wouldn't reach this code path
    # but this raw type may be inaccurate for `list` types as it points to the items type,
    # e.g. the `T` in `list[T]`
    if none_index == 1:
        raw_type = args[0]
    else:
        raw_type = args[1]

    return _construct_type(value=value, type_=raw_type, outer_type=field.outer_type_)


# TODO: remove the need for outer_type
def _construct_type(*, value: object, type_: type, outer_type: type) -> object:
    # we need to use the origin class for any types that are subscripted generics
    # e.g. Dict[str, object]
    origin = get_origin(type_) or type_
    args = get_args(type_)

    if get_origin(outer_type) == dict and is_mapping(value):
        _, items_type = get_args(outer_type)  # Dict[_, items_type]
        return {
            key: _construct_type(value=item, type_=items_type, outer_type=items_type) for key, item in value.items()
        }

    if origin == float:
        try:
            return float(value)  # type: ignore
        except Exception:
            return value

    if origin == int:
        try:
            return int(value)  # type: ignore
        except Exception:
            return value

    if not is_literal_type(type_) and (issubclass(origin, BaseModel) or issubclass(origin, GenericModel)):
        if is_list(value):
            return [cast(Any, type_).construct(**entry) if is_mapping(entry) else entry for entry in value]

        if is_mapping(value):
            if issubclass(type_, BaseModel):
                return type_.construct(**value)  # type: ignore[arg-type]

            return cast(Any, outer_type).construct(**value)

    if origin == list and is_list(value):
        inner_type = args[0]  # List[inner_type]
        return [_construct_type(value=entry, type_=inner_type, outer_type=inner_type) for entry in value]

    return value


class GenericModel(BaseModel, pydantic.generics.GenericModel):
    pass


@final
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
    json_data: Union[Body, None] = None
    extra_json: Union[AnyMapping, None] = None

    class Config(pydantic.BaseConfig):
        arbitrary_types_allowed: bool = True

    def get_max_retries(self, max_retries: int) -> int:
        if isinstance(self.max_retries, NotGiven):
            return max_retries
        return self.max_retries

    # override the `construct` method so that we can run custom transformations.
    # this is necessary as we don't want to do any actual runtime type checking
    # (which means we can't use validators) but we do want to ensure that `NotGiven`
    # values are not present
    @classmethod
    def construct(cls, _fields_set: set[str] | None = None, **values: object) -> FinalRequestOptions:
        kwargs = {
            # we unconditionally call `strip_not_given` on any value
            # as it will just ignore any non-mapping types
            key: strip_not_given(value)
            for key, value in values.items()
        }
        return super().construct(_fields_set, **kwargs)
