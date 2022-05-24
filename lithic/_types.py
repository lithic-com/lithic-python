from typing import Any, Dict, Union, Mapping, TypeVar

import pydantic
from httpx import Proxy, Timeout, BaseTransport
from typing_extensions import TypedDict

Transport = BaseTransport
Query = Mapping[str, object]
ModelT = TypeVar("ModelT", bound=pydantic.BaseModel)

# Approximates httpx internal ProxiesTypes
ProxiesTypes = Union[str, Proxy, Dict[str, Union[None, str, Proxy]]]


class RequestOptions(TypedDict, total=False):
    headers: Dict[str, str]
    max_retries: int
    timeout: Union[float, Timeout]


class FinalRequestOptions(TypedDict, total=False):
    method: str
    url: str
    json: Any
    params: Any
    headers: Dict[str, str]
    max_retries: int
    timeout: Union[float, Timeout, None]
