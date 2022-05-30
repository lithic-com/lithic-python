from typing import Dict, Union, Mapping, TypeVar

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


# Sentinel class used until PEP 0661 is accepted
class NotGiven:
    """For certain parameters such as `timeout=...` the intent can be made more clear
    by typing the parameter with this class rather than using None, for example:

    ```py
    def get(timeout: Union[int, NotGiven] = NotGiven()) -> Response: ...
    ```

    relays the intention more clearly than:

    ```py
    def get(timeout: Optional[int] = None) -> Response: ...
    ```

    This solution also allows you to indicate an "unset" state that is uniquely distinct
    from `None` which means you can explicitly pass `None` to disable the timeout entirely.
    """
