# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Dict, Union, Mapping, Optional
from typing_extensions import Literal

from . import resources
from ._qs import Querystring
from .types import APIStatus
from ._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._version import __version__
from ._base_client import (
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Lithic",
    "AsyncLithic",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.lithic.com/v1",
    "sandbox": "https://sandbox.lithic.com/v1",
}


class Lithic(SyncAPIClient):
    accounts: resources.Accounts
    account_holders: resources.AccountHolders
    auth_rules: resources.AuthRules
    auth_stream_enrollment: resources.AuthStreamEnrollmentResource
    cards: resources.Cards
    events: resources.Events
    funding_sources: resources.FundingSources
    transactions: resources.Transactions

    # client options
    api_key: str

    _environment: Literal["production", "sandbox"]

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
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
        """Construct a new synchronous lithic client instance.

        This automatically infers the `api_key` argument from the `LITHIC_API_KEY` environment variable if it is not provided.
        """
        api_key = api_key or os.environ.get("LITHIC_API_KEY", "")
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the LITHIC_API_KEY environment variable"
            )

        self._environment = environment

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_key = api_key

        self.accounts = resources.Accounts(self)
        self.account_holders = resources.AccountHolders(self)
        self.auth_rules = resources.AuthRules(self)
        self.auth_stream_enrollment = resources.AuthStreamEnrollmentResource(self)
        self.cards = resources.Cards(self)
        self.events = resources.Events(self)
        self.funding_sources = resources.FundingSources(self)
        self.transactions = resources.Transactions(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> Dict[str, str]:
        return {"Authorization": self.api_key}

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> Lithic:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def api_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> APIStatus:
        """API status check"""
        return self.get(
            "/status",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=APIStatus,
        )


class AsyncLithic(AsyncAPIClient):
    accounts: resources.AsyncAccounts
    account_holders: resources.AsyncAccountHolders
    auth_rules: resources.AsyncAuthRules
    auth_stream_enrollment: resources.AsyncAuthStreamEnrollmentResource
    cards: resources.AsyncCards
    events: resources.AsyncEvents
    funding_sources: resources.AsyncFundingSources
    transactions: resources.AsyncTransactions

    # client options
    api_key: str

    _environment: Literal["production", "sandbox"]

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
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
        """Construct a new async lithic client instance.

        This automatically infers the `api_key` argument from the `LITHIC_API_KEY` environment variable if it is not provided.
        """
        api_key = api_key or os.environ.get("LITHIC_API_KEY", "")
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the LITHIC_API_KEY environment variable"
            )

        self._environment = environment

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_key = api_key

        self.accounts = resources.AsyncAccounts(self)
        self.account_holders = resources.AsyncAccountHolders(self)
        self.auth_rules = resources.AsyncAuthRules(self)
        self.auth_stream_enrollment = resources.AsyncAuthStreamEnrollmentResource(self)
        self.cards = resources.AsyncCards(self)
        self.events = resources.AsyncEvents(self)
        self.funding_sources = resources.AsyncFundingSources(self)
        self.transactions = resources.AsyncTransactions(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> Dict[str, str]:
        return {"Authorization": self.api_key}

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> AsyncLithic:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def api_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> APIStatus:
        """API status check"""
        return await self.get(
            "/status",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=APIStatus,
        )


Client = Lithic

AsyncClient = AsyncLithic
