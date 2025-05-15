# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions, _legacy_response
from ._qs import Querystring
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
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LithicError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.api_status import APIStatus

if TYPE_CHECKING:
    from .resources import (
        cards,
        events,
        reports,
        accounts,
        balances,
        disputes,
        payments,
        three_ds,
        webhooks,
        auth_rules,
        transactions,
        card_programs,
        tokenizations,
        book_transfers,
        funding_events,
        account_holders,
        credit_products,
        digital_card_art,
        external_payments,
        aggregate_balances,
        financial_accounts,
        responder_endpoints,
        management_operations,
        auth_stream_enrollment,
        external_bank_accounts,
        tokenization_decisioning,
    )
    from .resources.accounts import Accounts, AsyncAccounts
    from .resources.balances import Balances, AsyncBalances
    from .resources.disputes import Disputes, AsyncDisputes
    from .resources.payments import Payments, AsyncPayments
    from .resources.cards.cards import Cards, AsyncCards
    from .resources.card_programs import CardPrograms, AsyncCardPrograms
    from .resources.events.events import Events, AsyncEvents
    from .resources.tokenizations import Tokenizations, AsyncTokenizations
    from .resources.book_transfers import BookTransfers, AsyncBookTransfers
    from .resources.funding_events import FundingEvents, AsyncFundingEvents
    from .resources.account_holders import AccountHolders, AsyncAccountHolders
    from .resources.reports.reports import Reports, AsyncReports
    from .resources.digital_card_art import DigitalCardArtResource, AsyncDigitalCardArtResource
    from .resources.external_payments import ExternalPayments, AsyncExternalPayments
    from .resources.three_ds.three_ds import ThreeDS, AsyncThreeDS
    from .resources.aggregate_balances import AggregateBalances, AsyncAggregateBalances
    from .resources.responder_endpoints import ResponderEndpoints, AsyncResponderEndpoints
    from .resources.auth_rules.auth_rules import AuthRules, AsyncAuthRules
    from .resources.management_operations import ManagementOperations, AsyncManagementOperations
    from .resources.auth_stream_enrollment import AuthStreamEnrollment, AsyncAuthStreamEnrollment
    from .resources.tokenization_decisioning import TokenizationDecisioning, AsyncTokenizationDecisioning
    from .resources.transactions.transactions import Transactions, AsyncTransactions
    from .resources.credit_products.credit_products import CreditProducts, AsyncCreditProducts
    from .resources.financial_accounts.financial_accounts import FinancialAccounts, AsyncFinancialAccounts
    from .resources.external_bank_accounts.external_bank_accounts import ExternalBankAccounts, AsyncExternalBankAccounts

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Lithic",
    "AsyncLithic",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.lithic.com",
    "sandbox": "https://sandbox.lithic.com",
}


class Lithic(SyncAPIClient):
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
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
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
        """Construct a new synchronous Lithic client instance.

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
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> Accounts:
        from .resources.accounts import Accounts

        return Accounts(self)

    @cached_property
    def account_holders(self) -> AccountHolders:
        from .resources.account_holders import AccountHolders

        return AccountHolders(self)

    @cached_property
    def auth_rules(self) -> AuthRules:
        from .resources.auth_rules import AuthRules

        return AuthRules(self)

    @cached_property
    def auth_stream_enrollment(self) -> AuthStreamEnrollment:
        from .resources.auth_stream_enrollment import AuthStreamEnrollment

        return AuthStreamEnrollment(self)

    @cached_property
    def tokenization_decisioning(self) -> TokenizationDecisioning:
        from .resources.tokenization_decisioning import TokenizationDecisioning

        return TokenizationDecisioning(self)

    @cached_property
    def tokenizations(self) -> Tokenizations:
        from .resources.tokenizations import Tokenizations

        return Tokenizations(self)

    @cached_property
    def cards(self) -> Cards:
        from .resources.cards import Cards

        return Cards(self)

    @cached_property
    def balances(self) -> Balances:
        from .resources.balances import Balances

        return Balances(self)

    @cached_property
    def aggregate_balances(self) -> AggregateBalances:
        from .resources.aggregate_balances import AggregateBalances

        return AggregateBalances(self)

    @cached_property
    def disputes(self) -> Disputes:
        from .resources.disputes import Disputes

        return Disputes(self)

    @cached_property
    def events(self) -> Events:
        from .resources.events import Events

        return Events(self)

    @cached_property
    def financial_accounts(self) -> FinancialAccounts:
        from .resources.financial_accounts import FinancialAccounts

        return FinancialAccounts(self)

    @cached_property
    def transactions(self) -> Transactions:
        from .resources.transactions import Transactions

        return Transactions(self)

    @cached_property
    def responder_endpoints(self) -> ResponderEndpoints:
        from .resources.responder_endpoints import ResponderEndpoints

        return ResponderEndpoints(self)

    @cached_property
    def external_bank_accounts(self) -> ExternalBankAccounts:
        from .resources.external_bank_accounts import ExternalBankAccounts

        return ExternalBankAccounts(self)

    @cached_property
    def payments(self) -> Payments:
        from .resources.payments import Payments

        return Payments(self)

    @cached_property
    def three_ds(self) -> ThreeDS:
        from .resources.three_ds import ThreeDS

        return ThreeDS(self)

    @cached_property
    def reports(self) -> Reports:
        from .resources.reports import Reports

        return Reports(self)

    @cached_property
    def card_programs(self) -> CardPrograms:
        from .resources.card_programs import CardPrograms

        return CardPrograms(self)

    @cached_property
    def digital_card_art(self) -> DigitalCardArtResource:
        from .resources.digital_card_art import DigitalCardArtResource

        return DigitalCardArtResource(self)

    @cached_property
    def book_transfers(self) -> BookTransfers:
        from .resources.book_transfers import BookTransfers

        return BookTransfers(self)

    @cached_property
    def credit_products(self) -> CreditProducts:
        from .resources.credit_products import CreditProducts

        return CreditProducts(self)

    @cached_property
    def external_payments(self) -> ExternalPayments:
        from .resources.external_payments import ExternalPayments

        return ExternalPayments(self)

    @cached_property
    def management_operations(self) -> ManagementOperations:
        from .resources.management_operations import ManagementOperations

        return ManagementOperations(self)

    @cached_property
    def funding_events(self) -> FundingEvents:
        from .resources.funding_events import FundingEvents

        return FundingEvents(self)
    
    @cached_property
    def webhooks(self) -> webhooks.Webhooks:
        from .resources.webhooks import Webhooks

        return Webhooks(self)

    @cached_property
    def with_raw_response(self) -> LithicWithRawResponse:
        return LithicWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LithicWithStreamedResponse:
        return LithicWithStreamedResponse(self)

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

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIStatus:
        """Status of api"""
        return self.get(
            "/v1/status",
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
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
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
        """Construct a new async AsyncLithic client instance.

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
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> AsyncAccounts:
        from .resources.accounts import AsyncAccounts

        return AsyncAccounts(self)

    @cached_property
    def account_holders(self) -> AsyncAccountHolders:
        from .resources.account_holders import AsyncAccountHolders

        return AsyncAccountHolders(self)

    @cached_property
    def auth_rules(self) -> AsyncAuthRules:
        from .resources.auth_rules import AsyncAuthRules

        return AsyncAuthRules(self)

    @cached_property
    def auth_stream_enrollment(self) -> AsyncAuthStreamEnrollment:
        from .resources.auth_stream_enrollment import AsyncAuthStreamEnrollment

        return AsyncAuthStreamEnrollment(self)

    @cached_property
    def tokenization_decisioning(self) -> AsyncTokenizationDecisioning:
        from .resources.tokenization_decisioning import AsyncTokenizationDecisioning

        return AsyncTokenizationDecisioning(self)

    @cached_property
    def tokenizations(self) -> AsyncTokenizations:
        from .resources.tokenizations import AsyncTokenizations

        return AsyncTokenizations(self)

    @cached_property
    def cards(self) -> AsyncCards:
        from .resources.cards import AsyncCards

        return AsyncCards(self)

    @cached_property
    def balances(self) -> AsyncBalances:
        from .resources.balances import AsyncBalances

        return AsyncBalances(self)

    @cached_property
    def aggregate_balances(self) -> AsyncAggregateBalances:
        from .resources.aggregate_balances import AsyncAggregateBalances

        return AsyncAggregateBalances(self)

    @cached_property
    def disputes(self) -> AsyncDisputes:
        from .resources.disputes import AsyncDisputes

        return AsyncDisputes(self)

    @cached_property
    def events(self) -> AsyncEvents:
        from .resources.events import AsyncEvents

        return AsyncEvents(self)

    @cached_property
    def financial_accounts(self) -> AsyncFinancialAccounts:
        from .resources.financial_accounts import AsyncFinancialAccounts

        return AsyncFinancialAccounts(self)

    @cached_property
    def transactions(self) -> AsyncTransactions:
        from .resources.transactions import AsyncTransactions

        return AsyncTransactions(self)

    @cached_property
    def responder_endpoints(self) -> AsyncResponderEndpoints:
        from .resources.responder_endpoints import AsyncResponderEndpoints

        return AsyncResponderEndpoints(self)

    @cached_property
    def external_bank_accounts(self) -> AsyncExternalBankAccounts:
        from .resources.external_bank_accounts import AsyncExternalBankAccounts

        return AsyncExternalBankAccounts(self)

    @cached_property
    def payments(self) -> AsyncPayments:
        from .resources.payments import AsyncPayments

        return AsyncPayments(self)

    @cached_property
    def three_ds(self) -> AsyncThreeDS:
        from .resources.three_ds import AsyncThreeDS

        return AsyncThreeDS(self)

    @cached_property
    def reports(self) -> AsyncReports:
        from .resources.reports import AsyncReports

        return AsyncReports(self)

    @cached_property
    def card_programs(self) -> AsyncCardPrograms:
        from .resources.card_programs import AsyncCardPrograms

        return AsyncCardPrograms(self)

    @cached_property
    def digital_card_art(self) -> AsyncDigitalCardArtResource:
        from .resources.digital_card_art import AsyncDigitalCardArtResource

        return AsyncDigitalCardArtResource(self)

    @cached_property
    def book_transfers(self) -> AsyncBookTransfers:
        from .resources.book_transfers import AsyncBookTransfers

        return AsyncBookTransfers(self)

    @cached_property
    def credit_products(self) -> AsyncCreditProducts:
        from .resources.credit_products import AsyncCreditProducts

        return AsyncCreditProducts(self)

    @cached_property
    def external_payments(self) -> AsyncExternalPayments:
        from .resources.external_payments import AsyncExternalPayments

        return AsyncExternalPayments(self)

    @cached_property
    def management_operations(self) -> AsyncManagementOperations:
        from .resources.management_operations import AsyncManagementOperations

        return AsyncManagementOperations(self)

    @cached_property
    def funding_events(self) -> AsyncFundingEvents:
        from .resources.funding_events import AsyncFundingEvents

        return AsyncFundingEvents(self)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooks:
        from .resources.webhooks import AsyncWebhooks

        return AsyncWebhooks(self)

    @cached_property
    def with_raw_response(self) -> AsyncLithicWithRawResponse:
        return AsyncLithicWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLithicWithStreamedResponse:
        return AsyncLithicWithStreamedResponse(self)

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

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIStatus:
        """Status of api"""
        return await self.get(
            "/v1/status",
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
    _client: Lithic

    def __init__(self, client: Lithic) -> None:
        self._client = client

        self.api_status = _legacy_response.to_raw_response_wrapper(
            client.api_status,
        )

    @cached_property
    def accounts(self) -> accounts.AccountsWithRawResponse:
        from .resources.accounts import AccountsWithRawResponse

        return AccountsWithRawResponse(self._client.accounts)

    @cached_property
    def account_holders(self) -> account_holders.AccountHoldersWithRawResponse:
        from .resources.account_holders import AccountHoldersWithRawResponse

        return AccountHoldersWithRawResponse(self._client.account_holders)

    @cached_property
    def auth_rules(self) -> auth_rules.AuthRulesWithRawResponse:
        from .resources.auth_rules import AuthRulesWithRawResponse

        return AuthRulesWithRawResponse(self._client.auth_rules)

    @cached_property
    def auth_stream_enrollment(self) -> auth_stream_enrollment.AuthStreamEnrollmentWithRawResponse:
        from .resources.auth_stream_enrollment import AuthStreamEnrollmentWithRawResponse

        return AuthStreamEnrollmentWithRawResponse(self._client.auth_stream_enrollment)

    @cached_property
    def tokenization_decisioning(self) -> tokenization_decisioning.TokenizationDecisioningWithRawResponse:
        from .resources.tokenization_decisioning import TokenizationDecisioningWithRawResponse

        return TokenizationDecisioningWithRawResponse(self._client.tokenization_decisioning)

    @cached_property
    def tokenizations(self) -> tokenizations.TokenizationsWithRawResponse:
        from .resources.tokenizations import TokenizationsWithRawResponse

        return TokenizationsWithRawResponse(self._client.tokenizations)

    @cached_property
    def cards(self) -> cards.CardsWithRawResponse:
        from .resources.cards import CardsWithRawResponse

        return CardsWithRawResponse(self._client.cards)

    @cached_property
    def balances(self) -> balances.BalancesWithRawResponse:
        from .resources.balances import BalancesWithRawResponse

        return BalancesWithRawResponse(self._client.balances)

    @cached_property
    def aggregate_balances(self) -> aggregate_balances.AggregateBalancesWithRawResponse:
        from .resources.aggregate_balances import AggregateBalancesWithRawResponse

        return AggregateBalancesWithRawResponse(self._client.aggregate_balances)

    @cached_property
    def disputes(self) -> disputes.DisputesWithRawResponse:
        from .resources.disputes import DisputesWithRawResponse

        return DisputesWithRawResponse(self._client.disputes)

    @cached_property
    def events(self) -> events.EventsWithRawResponse:
        from .resources.events import EventsWithRawResponse

        return EventsWithRawResponse(self._client.events)

    @cached_property
    def financial_accounts(self) -> financial_accounts.FinancialAccountsWithRawResponse:
        from .resources.financial_accounts import FinancialAccountsWithRawResponse

        return FinancialAccountsWithRawResponse(self._client.financial_accounts)

    @cached_property
    def transactions(self) -> transactions.TransactionsWithRawResponse:
        from .resources.transactions import TransactionsWithRawResponse

        return TransactionsWithRawResponse(self._client.transactions)

    @cached_property
    def responder_endpoints(self) -> responder_endpoints.ResponderEndpointsWithRawResponse:
        from .resources.responder_endpoints import ResponderEndpointsWithRawResponse

        return ResponderEndpointsWithRawResponse(self._client.responder_endpoints)

    @cached_property
    def external_bank_accounts(self) -> external_bank_accounts.ExternalBankAccountsWithRawResponse:
        from .resources.external_bank_accounts import ExternalBankAccountsWithRawResponse

        return ExternalBankAccountsWithRawResponse(self._client.external_bank_accounts)

    @cached_property
    def payments(self) -> payments.PaymentsWithRawResponse:
        from .resources.payments import PaymentsWithRawResponse

        return PaymentsWithRawResponse(self._client.payments)

    @cached_property
    def three_ds(self) -> three_ds.ThreeDSWithRawResponse:
        from .resources.three_ds import ThreeDSWithRawResponse

        return ThreeDSWithRawResponse(self._client.three_ds)

    @cached_property
    def reports(self) -> reports.ReportsWithRawResponse:
        from .resources.reports import ReportsWithRawResponse

        return ReportsWithRawResponse(self._client.reports)

    @cached_property
    def card_programs(self) -> card_programs.CardProgramsWithRawResponse:
        from .resources.card_programs import CardProgramsWithRawResponse

        return CardProgramsWithRawResponse(self._client.card_programs)

    @cached_property
    def digital_card_art(self) -> digital_card_art.DigitalCardArtResourceWithRawResponse:
        from .resources.digital_card_art import DigitalCardArtResourceWithRawResponse

        return DigitalCardArtResourceWithRawResponse(self._client.digital_card_art)

    @cached_property
    def book_transfers(self) -> book_transfers.BookTransfersWithRawResponse:
        from .resources.book_transfers import BookTransfersWithRawResponse

        return BookTransfersWithRawResponse(self._client.book_transfers)

    @cached_property
    def credit_products(self) -> credit_products.CreditProductsWithRawResponse:
        from .resources.credit_products import CreditProductsWithRawResponse

        return CreditProductsWithRawResponse(self._client.credit_products)

    @cached_property
    def external_payments(self) -> external_payments.ExternalPaymentsWithRawResponse:
        from .resources.external_payments import ExternalPaymentsWithRawResponse

        return ExternalPaymentsWithRawResponse(self._client.external_payments)

    @cached_property
    def management_operations(self) -> management_operations.ManagementOperationsWithRawResponse:
        from .resources.management_operations import ManagementOperationsWithRawResponse

        return ManagementOperationsWithRawResponse(self._client.management_operations)

    @cached_property
    def funding_events(self) -> funding_events.FundingEventsWithRawResponse:
        from .resources.funding_events import FundingEventsWithRawResponse

        return FundingEventsWithRawResponse(self._client.funding_events)


class AsyncLithicWithRawResponse:
    _client: AsyncLithic

    def __init__(self, client: AsyncLithic) -> None:
        self._client = client

        self.api_status = _legacy_response.async_to_raw_response_wrapper(
            client.api_status,
        )

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsWithRawResponse:
        from .resources.accounts import AsyncAccountsWithRawResponse

        return AsyncAccountsWithRawResponse(self._client.accounts)

    @cached_property
    def account_holders(self) -> account_holders.AsyncAccountHoldersWithRawResponse:
        from .resources.account_holders import AsyncAccountHoldersWithRawResponse

        return AsyncAccountHoldersWithRawResponse(self._client.account_holders)

    @cached_property
    def auth_rules(self) -> auth_rules.AsyncAuthRulesWithRawResponse:
        from .resources.auth_rules import AsyncAuthRulesWithRawResponse

        return AsyncAuthRulesWithRawResponse(self._client.auth_rules)

    @cached_property
    def auth_stream_enrollment(self) -> auth_stream_enrollment.AsyncAuthStreamEnrollmentWithRawResponse:
        from .resources.auth_stream_enrollment import AsyncAuthStreamEnrollmentWithRawResponse

        return AsyncAuthStreamEnrollmentWithRawResponse(self._client.auth_stream_enrollment)

    @cached_property
    def tokenization_decisioning(self) -> tokenization_decisioning.AsyncTokenizationDecisioningWithRawResponse:
        from .resources.tokenization_decisioning import AsyncTokenizationDecisioningWithRawResponse

        return AsyncTokenizationDecisioningWithRawResponse(self._client.tokenization_decisioning)

    @cached_property
    def tokenizations(self) -> tokenizations.AsyncTokenizationsWithRawResponse:
        from .resources.tokenizations import AsyncTokenizationsWithRawResponse

        return AsyncTokenizationsWithRawResponse(self._client.tokenizations)

    @cached_property
    def cards(self) -> cards.AsyncCardsWithRawResponse:
        from .resources.cards import AsyncCardsWithRawResponse

        return AsyncCardsWithRawResponse(self._client.cards)

    @cached_property
    def balances(self) -> balances.AsyncBalancesWithRawResponse:
        from .resources.balances import AsyncBalancesWithRawResponse

        return AsyncBalancesWithRawResponse(self._client.balances)

    @cached_property
    def aggregate_balances(self) -> aggregate_balances.AsyncAggregateBalancesWithRawResponse:
        from .resources.aggregate_balances import AsyncAggregateBalancesWithRawResponse

        return AsyncAggregateBalancesWithRawResponse(self._client.aggregate_balances)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesWithRawResponse:
        from .resources.disputes import AsyncDisputesWithRawResponse

        return AsyncDisputesWithRawResponse(self._client.disputes)

    @cached_property
    def events(self) -> events.AsyncEventsWithRawResponse:
        from .resources.events import AsyncEventsWithRawResponse

        return AsyncEventsWithRawResponse(self._client.events)

    @cached_property
    def financial_accounts(self) -> financial_accounts.AsyncFinancialAccountsWithRawResponse:
        from .resources.financial_accounts import AsyncFinancialAccountsWithRawResponse

        return AsyncFinancialAccountsWithRawResponse(self._client.financial_accounts)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsWithRawResponse:
        from .resources.transactions import AsyncTransactionsWithRawResponse

        return AsyncTransactionsWithRawResponse(self._client.transactions)

    @cached_property
    def responder_endpoints(self) -> responder_endpoints.AsyncResponderEndpointsWithRawResponse:
        from .resources.responder_endpoints import AsyncResponderEndpointsWithRawResponse

        return AsyncResponderEndpointsWithRawResponse(self._client.responder_endpoints)

    @cached_property
    def external_bank_accounts(self) -> external_bank_accounts.AsyncExternalBankAccountsWithRawResponse:
        from .resources.external_bank_accounts import AsyncExternalBankAccountsWithRawResponse

        return AsyncExternalBankAccountsWithRawResponse(self._client.external_bank_accounts)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsWithRawResponse:
        from .resources.payments import AsyncPaymentsWithRawResponse

        return AsyncPaymentsWithRawResponse(self._client.payments)

    @cached_property
    def three_ds(self) -> three_ds.AsyncThreeDSWithRawResponse:
        from .resources.three_ds import AsyncThreeDSWithRawResponse

        return AsyncThreeDSWithRawResponse(self._client.three_ds)

    @cached_property
    def reports(self) -> reports.AsyncReportsWithRawResponse:
        from .resources.reports import AsyncReportsWithRawResponse

        return AsyncReportsWithRawResponse(self._client.reports)

    @cached_property
    def card_programs(self) -> card_programs.AsyncCardProgramsWithRawResponse:
        from .resources.card_programs import AsyncCardProgramsWithRawResponse

        return AsyncCardProgramsWithRawResponse(self._client.card_programs)

    @cached_property
    def digital_card_art(self) -> digital_card_art.AsyncDigitalCardArtResourceWithRawResponse:
        from .resources.digital_card_art import AsyncDigitalCardArtResourceWithRawResponse

        return AsyncDigitalCardArtResourceWithRawResponse(self._client.digital_card_art)

    @cached_property
    def book_transfers(self) -> book_transfers.AsyncBookTransfersWithRawResponse:
        from .resources.book_transfers import AsyncBookTransfersWithRawResponse

        return AsyncBookTransfersWithRawResponse(self._client.book_transfers)

    @cached_property
    def credit_products(self) -> credit_products.AsyncCreditProductsWithRawResponse:
        from .resources.credit_products import AsyncCreditProductsWithRawResponse

        return AsyncCreditProductsWithRawResponse(self._client.credit_products)

    @cached_property
    def external_payments(self) -> external_payments.AsyncExternalPaymentsWithRawResponse:
        from .resources.external_payments import AsyncExternalPaymentsWithRawResponse

        return AsyncExternalPaymentsWithRawResponse(self._client.external_payments)

    @cached_property
    def management_operations(self) -> management_operations.AsyncManagementOperationsWithRawResponse:
        from .resources.management_operations import AsyncManagementOperationsWithRawResponse

        return AsyncManagementOperationsWithRawResponse(self._client.management_operations)

    @cached_property
    def funding_events(self) -> funding_events.AsyncFundingEventsWithRawResponse:
        from .resources.funding_events import AsyncFundingEventsWithRawResponse

        return AsyncFundingEventsWithRawResponse(self._client.funding_events)


class LithicWithStreamedResponse:
    _client: Lithic

    def __init__(self, client: Lithic) -> None:
        self._client = client

        self.api_status = to_streamed_response_wrapper(
            client.api_status,
        )

    @cached_property
    def accounts(self) -> accounts.AccountsWithStreamingResponse:
        from .resources.accounts import AccountsWithStreamingResponse

        return AccountsWithStreamingResponse(self._client.accounts)

    @cached_property
    def account_holders(self) -> account_holders.AccountHoldersWithStreamingResponse:
        from .resources.account_holders import AccountHoldersWithStreamingResponse

        return AccountHoldersWithStreamingResponse(self._client.account_holders)

    @cached_property
    def auth_rules(self) -> auth_rules.AuthRulesWithStreamingResponse:
        from .resources.auth_rules import AuthRulesWithStreamingResponse

        return AuthRulesWithStreamingResponse(self._client.auth_rules)

    @cached_property
    def auth_stream_enrollment(self) -> auth_stream_enrollment.AuthStreamEnrollmentWithStreamingResponse:
        from .resources.auth_stream_enrollment import AuthStreamEnrollmentWithStreamingResponse

        return AuthStreamEnrollmentWithStreamingResponse(self._client.auth_stream_enrollment)

    @cached_property
    def tokenization_decisioning(self) -> tokenization_decisioning.TokenizationDecisioningWithStreamingResponse:
        from .resources.tokenization_decisioning import TokenizationDecisioningWithStreamingResponse

        return TokenizationDecisioningWithStreamingResponse(self._client.tokenization_decisioning)

    @cached_property
    def tokenizations(self) -> tokenizations.TokenizationsWithStreamingResponse:
        from .resources.tokenizations import TokenizationsWithStreamingResponse

        return TokenizationsWithStreamingResponse(self._client.tokenizations)

    @cached_property
    def cards(self) -> cards.CardsWithStreamingResponse:
        from .resources.cards import CardsWithStreamingResponse

        return CardsWithStreamingResponse(self._client.cards)

    @cached_property
    def balances(self) -> balances.BalancesWithStreamingResponse:
        from .resources.balances import BalancesWithStreamingResponse

        return BalancesWithStreamingResponse(self._client.balances)

    @cached_property
    def aggregate_balances(self) -> aggregate_balances.AggregateBalancesWithStreamingResponse:
        from .resources.aggregate_balances import AggregateBalancesWithStreamingResponse

        return AggregateBalancesWithStreamingResponse(self._client.aggregate_balances)

    @cached_property
    def disputes(self) -> disputes.DisputesWithStreamingResponse:
        from .resources.disputes import DisputesWithStreamingResponse

        return DisputesWithStreamingResponse(self._client.disputes)

    @cached_property
    def events(self) -> events.EventsWithStreamingResponse:
        from .resources.events import EventsWithStreamingResponse

        return EventsWithStreamingResponse(self._client.events)

    @cached_property
    def financial_accounts(self) -> financial_accounts.FinancialAccountsWithStreamingResponse:
        from .resources.financial_accounts import FinancialAccountsWithStreamingResponse

        return FinancialAccountsWithStreamingResponse(self._client.financial_accounts)

    @cached_property
    def transactions(self) -> transactions.TransactionsWithStreamingResponse:
        from .resources.transactions import TransactionsWithStreamingResponse

        return TransactionsWithStreamingResponse(self._client.transactions)

    @cached_property
    def responder_endpoints(self) -> responder_endpoints.ResponderEndpointsWithStreamingResponse:
        from .resources.responder_endpoints import ResponderEndpointsWithStreamingResponse

        return ResponderEndpointsWithStreamingResponse(self._client.responder_endpoints)

    @cached_property
    def external_bank_accounts(self) -> external_bank_accounts.ExternalBankAccountsWithStreamingResponse:
        from .resources.external_bank_accounts import ExternalBankAccountsWithStreamingResponse

        return ExternalBankAccountsWithStreamingResponse(self._client.external_bank_accounts)

    @cached_property
    def payments(self) -> payments.PaymentsWithStreamingResponse:
        from .resources.payments import PaymentsWithStreamingResponse

        return PaymentsWithStreamingResponse(self._client.payments)

    @cached_property
    def three_ds(self) -> three_ds.ThreeDSWithStreamingResponse:
        from .resources.three_ds import ThreeDSWithStreamingResponse

        return ThreeDSWithStreamingResponse(self._client.three_ds)

    @cached_property
    def reports(self) -> reports.ReportsWithStreamingResponse:
        from .resources.reports import ReportsWithStreamingResponse

        return ReportsWithStreamingResponse(self._client.reports)

    @cached_property
    def card_programs(self) -> card_programs.CardProgramsWithStreamingResponse:
        from .resources.card_programs import CardProgramsWithStreamingResponse

        return CardProgramsWithStreamingResponse(self._client.card_programs)

    @cached_property
    def digital_card_art(self) -> digital_card_art.DigitalCardArtResourceWithStreamingResponse:
        from .resources.digital_card_art import DigitalCardArtResourceWithStreamingResponse

        return DigitalCardArtResourceWithStreamingResponse(self._client.digital_card_art)

    @cached_property
    def book_transfers(self) -> book_transfers.BookTransfersWithStreamingResponse:
        from .resources.book_transfers import BookTransfersWithStreamingResponse

        return BookTransfersWithStreamingResponse(self._client.book_transfers)

    @cached_property
    def credit_products(self) -> credit_products.CreditProductsWithStreamingResponse:
        from .resources.credit_products import CreditProductsWithStreamingResponse

        return CreditProductsWithStreamingResponse(self._client.credit_products)

    @cached_property
    def external_payments(self) -> external_payments.ExternalPaymentsWithStreamingResponse:
        from .resources.external_payments import ExternalPaymentsWithStreamingResponse

        return ExternalPaymentsWithStreamingResponse(self._client.external_payments)

    @cached_property
    def management_operations(self) -> management_operations.ManagementOperationsWithStreamingResponse:
        from .resources.management_operations import ManagementOperationsWithStreamingResponse

        return ManagementOperationsWithStreamingResponse(self._client.management_operations)

    @cached_property
    def funding_events(self) -> funding_events.FundingEventsWithStreamingResponse:
        from .resources.funding_events import FundingEventsWithStreamingResponse

        return FundingEventsWithStreamingResponse(self._client.funding_events)


class AsyncLithicWithStreamedResponse:
    _client: AsyncLithic

    def __init__(self, client: AsyncLithic) -> None:
        self._client = client

        self.api_status = async_to_streamed_response_wrapper(
            client.api_status,
        )

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsWithStreamingResponse:
        from .resources.accounts import AsyncAccountsWithStreamingResponse

        return AsyncAccountsWithStreamingResponse(self._client.accounts)

    @cached_property
    def account_holders(self) -> account_holders.AsyncAccountHoldersWithStreamingResponse:
        from .resources.account_holders import AsyncAccountHoldersWithStreamingResponse

        return AsyncAccountHoldersWithStreamingResponse(self._client.account_holders)

    @cached_property
    def auth_rules(self) -> auth_rules.AsyncAuthRulesWithStreamingResponse:
        from .resources.auth_rules import AsyncAuthRulesWithStreamingResponse

        return AsyncAuthRulesWithStreamingResponse(self._client.auth_rules)

    @cached_property
    def auth_stream_enrollment(self) -> auth_stream_enrollment.AsyncAuthStreamEnrollmentWithStreamingResponse:
        from .resources.auth_stream_enrollment import AsyncAuthStreamEnrollmentWithStreamingResponse

        return AsyncAuthStreamEnrollmentWithStreamingResponse(self._client.auth_stream_enrollment)

    @cached_property
    def tokenization_decisioning(self) -> tokenization_decisioning.AsyncTokenizationDecisioningWithStreamingResponse:
        from .resources.tokenization_decisioning import AsyncTokenizationDecisioningWithStreamingResponse

        return AsyncTokenizationDecisioningWithStreamingResponse(self._client.tokenization_decisioning)

    @cached_property
    def tokenizations(self) -> tokenizations.AsyncTokenizationsWithStreamingResponse:
        from .resources.tokenizations import AsyncTokenizationsWithStreamingResponse

        return AsyncTokenizationsWithStreamingResponse(self._client.tokenizations)

    @cached_property
    def cards(self) -> cards.AsyncCardsWithStreamingResponse:
        from .resources.cards import AsyncCardsWithStreamingResponse

        return AsyncCardsWithStreamingResponse(self._client.cards)

    @cached_property
    def balances(self) -> balances.AsyncBalancesWithStreamingResponse:
        from .resources.balances import AsyncBalancesWithStreamingResponse

        return AsyncBalancesWithStreamingResponse(self._client.balances)

    @cached_property
    def aggregate_balances(self) -> aggregate_balances.AsyncAggregateBalancesWithStreamingResponse:
        from .resources.aggregate_balances import AsyncAggregateBalancesWithStreamingResponse

        return AsyncAggregateBalancesWithStreamingResponse(self._client.aggregate_balances)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesWithStreamingResponse:
        from .resources.disputes import AsyncDisputesWithStreamingResponse

        return AsyncDisputesWithStreamingResponse(self._client.disputes)

    @cached_property
    def events(self) -> events.AsyncEventsWithStreamingResponse:
        from .resources.events import AsyncEventsWithStreamingResponse

        return AsyncEventsWithStreamingResponse(self._client.events)

    @cached_property
    def financial_accounts(self) -> financial_accounts.AsyncFinancialAccountsWithStreamingResponse:
        from .resources.financial_accounts import AsyncFinancialAccountsWithStreamingResponse

        return AsyncFinancialAccountsWithStreamingResponse(self._client.financial_accounts)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsWithStreamingResponse:
        from .resources.transactions import AsyncTransactionsWithStreamingResponse

        return AsyncTransactionsWithStreamingResponse(self._client.transactions)

    @cached_property
    def responder_endpoints(self) -> responder_endpoints.AsyncResponderEndpointsWithStreamingResponse:
        from .resources.responder_endpoints import AsyncResponderEndpointsWithStreamingResponse

        return AsyncResponderEndpointsWithStreamingResponse(self._client.responder_endpoints)

    @cached_property
    def external_bank_accounts(self) -> external_bank_accounts.AsyncExternalBankAccountsWithStreamingResponse:
        from .resources.external_bank_accounts import AsyncExternalBankAccountsWithStreamingResponse

        return AsyncExternalBankAccountsWithStreamingResponse(self._client.external_bank_accounts)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsWithStreamingResponse:
        from .resources.payments import AsyncPaymentsWithStreamingResponse

        return AsyncPaymentsWithStreamingResponse(self._client.payments)

    @cached_property
    def three_ds(self) -> three_ds.AsyncThreeDSWithStreamingResponse:
        from .resources.three_ds import AsyncThreeDSWithStreamingResponse

        return AsyncThreeDSWithStreamingResponse(self._client.three_ds)

    @cached_property
    def reports(self) -> reports.AsyncReportsWithStreamingResponse:
        from .resources.reports import AsyncReportsWithStreamingResponse

        return AsyncReportsWithStreamingResponse(self._client.reports)

    @cached_property
    def card_programs(self) -> card_programs.AsyncCardProgramsWithStreamingResponse:
        from .resources.card_programs import AsyncCardProgramsWithStreamingResponse

        return AsyncCardProgramsWithStreamingResponse(self._client.card_programs)

    @cached_property
    def digital_card_art(self) -> digital_card_art.AsyncDigitalCardArtResourceWithStreamingResponse:
        from .resources.digital_card_art import AsyncDigitalCardArtResourceWithStreamingResponse

        return AsyncDigitalCardArtResourceWithStreamingResponse(self._client.digital_card_art)

    @cached_property
    def book_transfers(self) -> book_transfers.AsyncBookTransfersWithStreamingResponse:
        from .resources.book_transfers import AsyncBookTransfersWithStreamingResponse

        return AsyncBookTransfersWithStreamingResponse(self._client.book_transfers)

    @cached_property
    def credit_products(self) -> credit_products.AsyncCreditProductsWithStreamingResponse:
        from .resources.credit_products import AsyncCreditProductsWithStreamingResponse

        return AsyncCreditProductsWithStreamingResponse(self._client.credit_products)

    @cached_property
    def external_payments(self) -> external_payments.AsyncExternalPaymentsWithStreamingResponse:
        from .resources.external_payments import AsyncExternalPaymentsWithStreamingResponse

        return AsyncExternalPaymentsWithStreamingResponse(self._client.external_payments)

    @cached_property
    def management_operations(self) -> management_operations.AsyncManagementOperationsWithStreamingResponse:
        from .resources.management_operations import AsyncManagementOperationsWithStreamingResponse

        return AsyncManagementOperationsWithStreamingResponse(self._client.management_operations)

    @cached_property
    def funding_events(self) -> funding_events.AsyncFundingEventsWithStreamingResponse:
        from .resources.funding_events import AsyncFundingEventsWithStreamingResponse

        return AsyncFundingEventsWithStreamingResponse(self._client.funding_events)


Client = Lithic

AsyncClient = AsyncLithic
