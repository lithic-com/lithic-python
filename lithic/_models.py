from __future__ import annotations

from typing import Any, Type, Union, cast

import pydantic
import pydantic.generics
from pydantic.typing import is_literal_type

from ._types import Query, ModelT, Headers, Timeout, NotGiven, RequestFiles

__all__ = ["BaseModel", "GenericModel"]


class BaseModel(pydantic.BaseModel):
    # Override the 'construct' method in a way that supports recursive parsing without validation.
    # Based on https://github.com/samuelcolvin/pydantic/issues/1168#issuecomment-817742836.
    @classmethod
    def construct(cls: Type[ModelT], _fields_set: set[str] | None = None, **values: object) -> ModelT:
        m = cls.__new__(cls)
        fields_values = {}

        config = cls.__config__

        for name, field in cls.__fields__.items():
            key = field.alias
            if key not in values and config.allow_population_by_field_name:
                key = name

            if key in values:
                if values[key] is None:
                    fields_values[name] = field.get_default()
                else:
                    if not is_literal_type(field.type_) and (
                        issubclass(field.type_, BaseModel) or issubclass(field.type_, GenericModel)
                    ):
                        if field.shape == 2:
                            # field.shape == 2 signifies a List
                            # TODO: should we validate that this is actually a list at runtime?
                            fields_values[name] = [field.type_.construct(**e) for e in cast(Any, values[key])]
                        else:
                            fields_values[name] = field.outer_type_.construct(**values[key])
                    else:
                        fields_values[name] = values[key]
            elif not field.required:
                fields_values[name] = field.get_default()

        object.__setattr__(m, "__dict__", fields_values)
        if _fields_set is None:
            _fields_set = set(values.keys())
        object.__setattr__(m, "__fields_set__", _fields_set)
        m._init_private_attributes()
        return m


class GenericModel(BaseModel, pydantic.generics.GenericModel):
    pass


class FinalRequestOptions(BaseModel):
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
    json_data: Union[object, None] = None

    class Config(pydantic.BaseConfig):
        arbitrary_types_allowed: bool = True

    def get_max_retries(self, max_retries: int) -> int:
        if isinstance(self.max_retries, NotGiven):
            return max_retries
        return self.max_retries
