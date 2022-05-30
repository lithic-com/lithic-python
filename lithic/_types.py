from typing import Dict, Union, Literal, Mapping, TypeVar

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
    timeout: Union[float, Timeout, None]


# Sentinel class used until PEP 0661 is accepted
class NotGiven:
    """
    A sentinel singleton class used to distinguish omitted keyword arguments
    from those passed in with the value None (which may have different behavior).

    For example:

    ```py
    def get(timeout: Union[int, NotGiven, None] = NotGiven()) -> Response: ...

    get(timout=1) # 1s timeout
    get(timout=None) # No timeout
    get() # Default timeout behavior, which may not be statically known at the method definition.
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False
