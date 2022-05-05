# File generated from our OpenAPI spec by Stainless.

__title__ = "lithic"
__version__ = "0.1.1"

import os
from typing import Optional, Union
from typing_extensions import TypedDict
from ._core import Timeout, Transport, ProxiesTypes, DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, RequestOptions
from ._client import SyncAPIClient, AsyncAPIClient
from . import resources
from . import types

from .exceptions import (
    APIError,
    APIConnectionError,
    APITimeoutError,
    APIResponseValidationError,
    BadRequestError,
    AuthenticationError,
    PermissionDeniedError,
    NotFoundError,
    ConflictError,
    UnprocessableEntityError,
    RateLimitError,
    InternalServerError,
    APIStatusError,
)

environments = {"production": "https://api.lithic.com/v1", "sandbox": "https://sandbox.lithic.com/v1"}

__all__ = [
    "environments",
    "Lithic",
    "AsyncLithic",
    "Client",
    "AsyncClient",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "types",
    "APIError",
    "APIConnectionError",
    "APITimeoutError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "APIStatusError",
]


class Lithic(SyncAPIClient):
    accounts: resources.Accounts
    account_holders: resources.AccountHolders
    auth_rules: resources.AuthRules
    auth_stream_enrollment: resources.AuthStreamEnrollmentResource
    cards: resources.Cards
    funding_sources: resources.FundingSources
    transactions: resources.Transactions
    status: resources.StatusResource

    def __init__(
        self,
        *,
        environment: str = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        api_key = api_key or os.environ.get("LITHIC_API_KEY", "")
        if not api_key:
            raise Exception("No API key provided")
        base_url = base_url or environments.get(environment or "") or ""

        super().__init__(
            version=__version__,
            base_url=base_url,
            api_key=api_key,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.Accounts(self)
        self.account_holders = resources.AccountHolders(self)
        self.auth_rules = resources.AuthRules(self)
        self.auth_stream_enrollment = resources.AuthStreamEnrollmentResource(self)
        self.cards = resources.Cards(self)
        self.funding_sources = resources.FundingSources(self)
        self.transactions = resources.Transactions(self)
        self.status = resources.StatusResource(self)

    def default_headers(self):
        header = f"api-key {self.api_key}"
        return {**super().default_headers(), "Authorization": header}


class AsyncLithic(AsyncAPIClient):
    accounts: resources.AsyncAccounts
    account_holders: resources.AsyncAccountHolders
    auth_rules: resources.AsyncAuthRules
    auth_stream_enrollment: resources.AsyncAuthStreamEnrollmentResource
    cards: resources.AsyncCards
    funding_sources: resources.AsyncFundingSources
    transactions: resources.AsyncTransactions
    status: resources.AsyncStatusResource

    def __init__(
        self,
        *,
        environment: str = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        api_key = api_key or os.environ.get("LITHIC_API_KEY", "")
        if not api_key:
            raise Exception("No API key provided")
        base_url = base_url or environments.get(environment or "") or ""

        super().__init__(
            version=__version__,
            base_url=base_url,
            api_key=api_key,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.AsyncAccounts(self)
        self.account_holders = resources.AsyncAccountHolders(self)
        self.auth_rules = resources.AsyncAuthRules(self)
        self.auth_stream_enrollment = resources.AsyncAuthStreamEnrollmentResource(self)
        self.cards = resources.AsyncCards(self)
        self.funding_sources = resources.AsyncFundingSources(self)
        self.transactions = resources.AsyncTransactions(self)
        self.status = resources.AsyncStatusResource(self)

    def default_headers(self):
        header = f"api-key {self.api_key}"
        return {**super().default_headers(), "Authorization": header}


class Client(Lithic):
    pass


class AsyncClient(AsyncLithic):
    pass
