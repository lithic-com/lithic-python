import inspect
import platform
import httpx
from typing import Dict, Generic, Iterable, Optional, Any, TypeVar, Union, Type
from typing_extensions import TypedDict
import json
from random import random
from ._models import NoneModel, IResponseModel, GenericModel
from abc import ABC, abstractmethod
from pydantic import PrivateAttr

DEFAULT_MAX_RETRIES = 2

Timeout = httpx.Timeout
DEFAULT_TIMEOUT = Timeout(timeout=60.0)

Transport = httpx.BaseTransport
# Approximates httpx internal ProxiesTypes
ProxiesTypes = Union[str, httpx.Proxy, Dict[str, Union[None, str, httpx.Proxy]]]

Req = TypeVar("Req")
Rsp = TypeVar("Rsp", bound=IResponseModel)


class RequestOptions(TypedDict, total=False):
    headers: Dict[str, str]
    max_retries: int
    timeout: Union[float, Timeout]


def make_request_options(
    headers,
    max_retries,
    timeout,
) -> RequestOptions:
    """Create a dict of type RequestOptions without keys of None values."""
    d = {
        "headers": headers,
        "max_retries": max_retries,
        "timeout": timeout,
    }
    filtered = {k: v for k, v in d.items() if v is not None}
    return RequestOptions(**filtered)  # type: ignore


class FinalRequestOptions(TypedDict, total=False):
    method: str
    url: str
    json: Any
    params: Any
    headers: Dict[str, str]
    max_retries: int
    timeout: Union[float, Timeout, None]


class BaseClient(ABC):
    _version: str
    api_key: str
    max_retries: int
    timeout: Union[float, Timeout, None]
    _strict_response_validation: bool

    def __init__(
        self,
        version: str,
        api_key: str,
        _strict_response_validation: bool,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
    ) -> None:
        self._version = version
        self.api_key = api_key
        self.max_retries = max_retries
        self.timeout = timeout
        self._strict_response_validation = _strict_response_validation

    def remaining_retries(
        self,
        remaining_retries: Optional[int],
        options: FinalRequestOptions,
    ) -> int:
        return remaining_retries if remaining_retries is not None else options.get("max_retries", self.max_retries)

    def prepare_request_args(
        self,
        options: FinalRequestOptions,
    ) -> Dict[str, Any]:
        headers = {**self.default_headers(), **options.get("headers", {})}
        req_args: Dict[str, Any] = {**options, "headers": headers, "timeout": options.get("timeout", self.timeout)}
        # ensure we only returned expected keyword arguments to `build_request()` to avoid a `TypeError: build_request()
        # got an unexpected keyword argument 'max_retries'`.
        expected_params = inspect.signature(httpx.Client.build_request).parameters.values()
        return {k: v for k, v in req_args.items() if k in [p.name for p in expected_params]}

    def process_response(self, model: Type[Rsp], options: FinalRequestOptions, response: httpx.Response) -> Rsp:
        if model is NoneModel:
            return model()
        data = (
            response.json()
            if response.headers.get("content-type") == "application/json"
            else {"content": response.text}
        )
        if self._strict_response_validation:
            return model(**data)
        else:
            return model.construct(**data)

    def default_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "User-Agent": self.user_agent(),
            "X-Stainless-Client-User-Agent": self.platform_properties(),
        }

    def user_agent(self) -> str:
        return f"{self.__class__.__name__}/Python {self._version}"

    def platform_properties(self) -> str:
        arch, _ = platform.architecture()
        properties = {
            "lang": "python",
            "packageVersion": self._version,
            "os": platform.system(),
            "arch": arch,
            "runtime": platform.python_implementation(),
            "runtimeVersion": platform.python_version(),
        }
        return json.dumps(properties)

    def calculate_retry_timeout(
        self,
        remaining_retries: int,
        options: FinalRequestOptions,
        response_headers: Optional[httpx.Headers] = None,
    ) -> float:
        max_retries = options.get("max_retries", self.max_retries)
        try:
            # About the Retry-After header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
            #
            # TODO: we may want to handle the case where the header is using the http-date syntax: "Retry-After:
            # <http-date>". See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After#syntax for
            # details.
            retry_after = -1 if response_headers is None else int(response_headers.get("retry-after"))
        except:
            retry_after = -1

        # If the API asks us to wait a certain amount of time (and it's a reasonable amount), just do what it says.
        if 0 < retry_after <= 60:
            return retry_after

        initial_retry_delay = 0.5
        max_retry_delay = 2.0
        nb_retries = max_retries - remaining_retries
        # Apply exponential backoff, but not more than the max.
        sleep_seconds = min(initial_retry_delay * pow(nb_retries - 1, 2), max_retry_delay)
        # Apply some jitter, plus-or-minus half a second.
        jitter = random() - 0.5
        timeout = sleep_seconds + jitter
        return timeout if timeout >= 0 else 0

    def should_retry(self, response: httpx.Response) -> bool:
        # Note: this is not a standard header
        shouldRetryHeader = response.headers.get("x-should-retry")

        # If the server explicitly says whether or not to retry, obey.
        if shouldRetryHeader == "true":
            return True
        if shouldRetryHeader == "false":
            return False

        # Retry on lock timeouts.
        if response.status_code == 409:
            return True
        # Retry on rate limits.
        if response.status_code == 429:
            return True
        # Retry internal errors.
        if response.status_code >= 500:
            return True
        return False


Page = TypeVar("Page")
Item = TypeVar("Item")
PageParams = TypeVar("PageParams")


class BasePage(GenericModel, Generic[Item, PageParams]):
    _options: FinalRequestOptions = PrivateAttr()

    def has_next_page(self) -> bool:  # type: ignore
        pass

    def next_page_params(self) -> Optional[PageParams]:  # type: ignore
        if self.has_next_page():
            return self._next_page_params()
        return None

    def _next_page_params(self) -> PageParams:  # type: ignore
        pass

    def _get_page_items(self) -> Iterable[Item]:  # type: ignore
        pass
