# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import asyncio
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from .types import APIStatus
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    AsyncTransport,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from ._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._exceptions import LithicError, APIStatusError
from ._base_client import (
    DEFAULT_LIMITS,
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
    tokenization_decisioning: resources.TokenizationDecisioning
    tokenizations: resources.Tokenizations
    cards: resources.Cards
    balances: resources.Balances
    aggregate_balances: resources.AggregateBalances
    disputes: resources.Disputes
    events: resources.Events
    financial_accounts: resources.FinancialAccounts
    transactions: resources.Transactions
    responder_endpoints: resources.ResponderEndpoints
    webhooks: resources.Webhooks
    external_bank_accounts: resources.ExternalBankAccounts
    payments: resources.Payments
    three_ds: resources.ThreeDS
    reports: resources.Reports
    card_product: resources.CardProduct
    card_programs: resources.CardPrograms
    digital_card_art: resources.DigitalCardArtResource
    with_raw_response: LithicWithRawResponse

    # client options
    api_key: str
    webhook_secret: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Transport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `LITHIC_API_KEY`
        - `webhook_secret` from `LITHIC_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("LITHIC_API_KEY")
        if api_key is None:
            raise LithicError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LITHIC_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("LITHIC_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        self._environment = environment

        base_url_env = os.environ.get("LITHIC_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LITHIC_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.Accounts(self)
        self.account_holders = resources.AccountHolders(self)
        self.auth_rules = resources.AuthRules(self)
        self.auth_stream_enrollment = resources.AuthStreamEnrollmentResource(self)
        self.tokenization_decisioning = resources.TokenizationDecisioning(self)
        self.tokenizations = resources.Tokenizations(self)
        self.cards = resources.Cards(self)
        self.balances = resources.Balances(self)
        self.aggregate_balances = resources.AggregateBalances(self)
        self.disputes = resources.Disputes(self)
        self.events = resources.Events(self)
        self.financial_accounts = resources.FinancialAccounts(self)
        self.transactions = resources.Transactions(self)
        self.responder_endpoints = resources.ResponderEndpoints(self)
        self.webhooks = resources.Webhooks(self)
        self.external_bank_accounts = resources.ExternalBankAccounts(self)
        self.payments = resources.Payments(self)
        self.three_ds = resources.ThreeDS(self)
        self.reports = resources.Reports(self)
        self.card_product = resources.CardProduct(self)
        self.card_programs = resources.CardPrograms(self)
        self.digital_card_art = resources.DigitalCardArtResource(self)
        self.with_raw_response = LithicWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Lithic-Pagination": "cursor",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        connection_pool_limits: httpx.Limits | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if self._has_custom_http_client:
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        if not hasattr(self, "_has_custom_http_client") or not hasattr(self, "close"):
            # this can happen if the '__init__' method raised an error
            return

        if self._has_custom_http_client:
            return

        self.close()

    def api_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIStatus:
        """API status check"""
        return self.get(
            "/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIStatus,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLithic(AsyncAPIClient):
    accounts: resources.AsyncAccounts
    account_holders: resources.AsyncAccountHolders
    auth_rules: resources.AsyncAuthRules
    auth_stream_enrollment: resources.AsyncAuthStreamEnrollmentResource
    tokenization_decisioning: resources.AsyncTokenizationDecisioning
    tokenizations: resources.AsyncTokenizations
    cards: resources.AsyncCards
    balances: resources.AsyncBalances
    aggregate_balances: resources.AsyncAggregateBalances
    disputes: resources.AsyncDisputes
    events: resources.AsyncEvents
    financial_accounts: resources.AsyncFinancialAccounts
    transactions: resources.AsyncTransactions
    responder_endpoints: resources.AsyncResponderEndpoints
    webhooks: resources.AsyncWebhooks
    external_bank_accounts: resources.AsyncExternalBankAccounts
    payments: resources.AsyncPayments
    three_ds: resources.AsyncThreeDS
    reports: resources.AsyncReports
    card_product: resources.AsyncCardProduct
    card_programs: resources.AsyncCardPrograms
    digital_card_art: resources.AsyncDigitalCardArtResource
    with_raw_response: AsyncLithicWithRawResponse

    # client options
    api_key: str
    webhook_secret: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: AsyncTransport | None = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: ProxiesTypes | None = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = None,
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `LITHIC_API_KEY`
        - `webhook_secret` from `LITHIC_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("LITHIC_API_KEY")
        if api_key is None:
            raise LithicError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LITHIC_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("LITHIC_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        self._environment = environment

        base_url_env = os.environ.get("LITHIC_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `LITHIC_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.accounts = resources.AsyncAccounts(self)
        self.account_holders = resources.AsyncAccountHolders(self)
        self.auth_rules = resources.AsyncAuthRules(self)
        self.auth_stream_enrollment = resources.AsyncAuthStreamEnrollmentResource(self)
        self.tokenization_decisioning = resources.AsyncTokenizationDecisioning(self)
        self.tokenizations = resources.AsyncTokenizations(self)
        self.cards = resources.AsyncCards(self)
        self.balances = resources.AsyncBalances(self)
        self.aggregate_balances = resources.AsyncAggregateBalances(self)
        self.disputes = resources.AsyncDisputes(self)
        self.events = resources.AsyncEvents(self)
        self.financial_accounts = resources.AsyncFinancialAccounts(self)
        self.transactions = resources.AsyncTransactions(self)
        self.responder_endpoints = resources.AsyncResponderEndpoints(self)
        self.webhooks = resources.AsyncWebhooks(self)
        self.external_bank_accounts = resources.AsyncExternalBankAccounts(self)
        self.payments = resources.AsyncPayments(self)
        self.three_ds = resources.AsyncThreeDS(self)
        self.reports = resources.AsyncReports(self)
        self.card_product = resources.AsyncCardProduct(self)
        self.card_programs = resources.AsyncCardPrograms(self)
        self.digital_card_art = resources.AsyncDigitalCardArtResource(self)
        self.with_raw_response = AsyncLithicWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Lithic-Pagination": "cursor",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        connection_pool_limits: httpx.Limits | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
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

        if connection_pool_limits is not None:
            if http_client is not None:
                raise ValueError("The 'http_client' argument is mutually exclusive with 'connection_pool_limits'")

            if self._has_custom_http_client:
                raise ValueError(
                    "A custom HTTP client has been set and is mutually exclusive with the 'connection_pool_limits' argument"
                )

            http_client = None
        else:
            if self._limits is not DEFAULT_LIMITS:
                connection_pool_limits = self._limits
            else:
                connection_pool_limits = None

            http_client = http_client or self._client

        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            connection_pool_limits=connection_pool_limits,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        if not hasattr(self, "_has_custom_http_client") or not hasattr(self, "close"):
            # this can happen if the '__init__' method raised an error
            return

        if self._has_custom_http_client:
            return

        try:
            asyncio.get_running_loop().create_task(self.close())
        except Exception:
            pass

    async def api_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIStatus:
        """API status check"""
        return await self.get(
            "/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIStatus,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LithicWithRawResponse:
    def __init__(self, client: Lithic) -> None:
        self.accounts = resources.AccountsWithRawResponse(client.accounts)
        self.account_holders = resources.AccountHoldersWithRawResponse(client.account_holders)
        self.auth_rules = resources.AuthRulesWithRawResponse(client.auth_rules)
        self.auth_stream_enrollment = resources.AuthStreamEnrollmentResourceWithRawResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = resources.TokenizationDecisioningWithRawResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = resources.TokenizationsWithRawResponse(client.tokenizations)
        self.cards = resources.CardsWithRawResponse(client.cards)
        self.balances = resources.BalancesWithRawResponse(client.balances)
        self.aggregate_balances = resources.AggregateBalancesWithRawResponse(client.aggregate_balances)
        self.disputes = resources.DisputesWithRawResponse(client.disputes)
        self.events = resources.EventsWithRawResponse(client.events)
        self.financial_accounts = resources.FinancialAccountsWithRawResponse(client.financial_accounts)
        self.transactions = resources.TransactionsWithRawResponse(client.transactions)
        self.responder_endpoints = resources.ResponderEndpointsWithRawResponse(client.responder_endpoints)
        self.external_bank_accounts = resources.ExternalBankAccountsWithRawResponse(client.external_bank_accounts)
        self.payments = resources.PaymentsWithRawResponse(client.payments)
        self.three_ds = resources.ThreeDSWithRawResponse(client.three_ds)
        self.reports = resources.ReportsWithRawResponse(client.reports)
        self.card_product = resources.CardProductWithRawResponse(client.card_product)
        self.card_programs = resources.CardProgramsWithRawResponse(client.card_programs)
        self.digital_card_art = resources.DigitalCardArtResourceWithRawResponse(client.digital_card_art)

        self.api_status = to_raw_response_wrapper(
            client.api_status,
        )


class AsyncLithicWithRawResponse:
    def __init__(self, client: AsyncLithic) -> None:
        self.accounts = resources.AsyncAccountsWithRawResponse(client.accounts)
        self.account_holders = resources.AsyncAccountHoldersWithRawResponse(client.account_holders)
        self.auth_rules = resources.AsyncAuthRulesWithRawResponse(client.auth_rules)
        self.auth_stream_enrollment = resources.AsyncAuthStreamEnrollmentResourceWithRawResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = resources.AsyncTokenizationDecisioningWithRawResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = resources.AsyncTokenizationsWithRawResponse(client.tokenizations)
        self.cards = resources.AsyncCardsWithRawResponse(client.cards)
        self.balances = resources.AsyncBalancesWithRawResponse(client.balances)
        self.aggregate_balances = resources.AsyncAggregateBalancesWithRawResponse(client.aggregate_balances)
        self.disputes = resources.AsyncDisputesWithRawResponse(client.disputes)
        self.events = resources.AsyncEventsWithRawResponse(client.events)
        self.financial_accounts = resources.AsyncFinancialAccountsWithRawResponse(client.financial_accounts)
        self.transactions = resources.AsyncTransactionsWithRawResponse(client.transactions)
        self.responder_endpoints = resources.AsyncResponderEndpointsWithRawResponse(client.responder_endpoints)
        self.external_bank_accounts = resources.AsyncExternalBankAccountsWithRawResponse(client.external_bank_accounts)
        self.payments = resources.AsyncPaymentsWithRawResponse(client.payments)
        self.three_ds = resources.AsyncThreeDSWithRawResponse(client.three_ds)
        self.reports = resources.AsyncReportsWithRawResponse(client.reports)
        self.card_product = resources.AsyncCardProductWithRawResponse(client.card_product)
        self.card_programs = resources.AsyncCardProgramsWithRawResponse(client.card_programs)
        self.digital_card_art = resources.AsyncDigitalCardArtResourceWithRawResponse(client.digital_card_art)

        self.api_status = async_to_raw_response_wrapper(
            client.api_status,
        )


Client = Lithic

AsyncClient = AsyncLithic
