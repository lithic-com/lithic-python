from typing import Mapping, TypeVar
import pydantic


Query = Mapping[str, object]
ModelT = TypeVar("ModelT", bound=pydantic.BaseModel)
