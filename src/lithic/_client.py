# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
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
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .resources import (
    accounts,
    balances,
    disputes,
    payments,
    webhooks,
    card_programs,
    tokenizations,
    book_transfers,
    account_holders,
    digital_card_art,
    external_payments,
    aggregate_balances,
    responder_endpoints,
    management_operations,
    auth_stream_enrollment,
    tokenization_decisioning,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LithicError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.cards import cards
from .resources.events import events
from .types.api_status import APIStatus
from .resources.reports import reports
from .resources.three_ds import three_ds
from .resources.auth_rules import auth_rules
from .resources.transactions import transactions
from .resources.credit_products import credit_products
from .resources.financial_accounts import financial_accounts
from .resources.external_bank_accounts import external_bank_accounts

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
    accounts: accounts.Accounts
    account_holders: account_holders.AccountHolders
    auth_rules: auth_rules.AuthRules
    auth_stream_enrollment: auth_stream_enrollment.AuthStreamEnrollment
    tokenization_decisioning: tokenization_decisioning.TokenizationDecisioning
    tokenizations: tokenizations.Tokenizations
    cards: cards.Cards
    balances: balances.Balances
    aggregate_balances: aggregate_balances.AggregateBalances
    disputes: disputes.Disputes
    events: events.Events
    financial_accounts: financial_accounts.FinancialAccounts
    transactions: transactions.Transactions
    responder_endpoints: responder_endpoints.ResponderEndpoints
    webhooks: webhooks.Webhooks
    external_bank_accounts: external_bank_accounts.ExternalBankAccounts
    payments: payments.Payments
    three_ds: three_ds.ThreeDS
    reports: reports.Reports
    card_programs: card_programs.CardPrograms
    digital_card_art: digital_card_art.DigitalCardArtResource
    book_transfers: book_transfers.BookTransfers
    credit_products: credit_products.CreditProducts
    external_payments: external_payments.ExternalPayments
    management_operations: management_operations.ManagementOperations
    with_raw_response: LithicWithRawResponse
    with_streaming_response: LithicWithStreamedResponse

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

        self.accounts = accounts.Accounts(self)
        self.account_holders = account_holders.AccountHolders(self)
        self.auth_rules = auth_rules.AuthRules(self)
        self.auth_stream_enrollment = auth_stream_enrollment.AuthStreamEnrollment(self)
        self.tokenization_decisioning = tokenization_decisioning.TokenizationDecisioning(self)
        self.tokenizations = tokenizations.Tokenizations(self)
        self.cards = cards.Cards(self)
        self.balances = balances.Balances(self)
        self.aggregate_balances = aggregate_balances.AggregateBalances(self)
        self.disputes = disputes.Disputes(self)
        self.events = events.Events(self)
        self.financial_accounts = financial_accounts.FinancialAccounts(self)
        self.transactions = transactions.Transactions(self)
        self.responder_endpoints = responder_endpoints.ResponderEndpoints(self)
        self.webhooks = webhooks.Webhooks(self)
        self.external_bank_accounts = external_bank_accounts.ExternalBankAccounts(self)
        self.payments = payments.Payments(self)
        self.three_ds = three_ds.ThreeDS(self)
        self.reports = reports.Reports(self)
        self.card_programs = card_programs.CardPrograms(self)
        self.digital_card_art = digital_card_art.DigitalCardArtResource(self)
        self.book_transfers = book_transfers.BookTransfers(self)
        self.credit_products = credit_products.CreditProducts(self)
        self.external_payments = external_payments.ExternalPayments(self)
        self.management_operations = management_operations.ManagementOperations(self)
        self.with_raw_response = LithicWithRawResponse(self)
        self.with_streaming_response = LithicWithStreamedResponse(self)

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
    accounts: accounts.AsyncAccounts
    account_holders: account_holders.AsyncAccountHolders
    auth_rules: auth_rules.AsyncAuthRules
    auth_stream_enrollment: auth_stream_enrollment.AsyncAuthStreamEnrollment
    tokenization_decisioning: tokenization_decisioning.AsyncTokenizationDecisioning
    tokenizations: tokenizations.AsyncTokenizations
    cards: cards.AsyncCards
    balances: balances.AsyncBalances
    aggregate_balances: aggregate_balances.AsyncAggregateBalances
    disputes: disputes.AsyncDisputes
    events: events.AsyncEvents
    financial_accounts: financial_accounts.AsyncFinancialAccounts
    transactions: transactions.AsyncTransactions
    responder_endpoints: responder_endpoints.AsyncResponderEndpoints
    webhooks: webhooks.AsyncWebhooks
    external_bank_accounts: external_bank_accounts.AsyncExternalBankAccounts
    payments: payments.AsyncPayments
    three_ds: three_ds.AsyncThreeDS
    reports: reports.AsyncReports
    card_programs: card_programs.AsyncCardPrograms
    digital_card_art: digital_card_art.AsyncDigitalCardArtResource
    book_transfers: book_transfers.AsyncBookTransfers
    credit_products: credit_products.AsyncCreditProducts
    external_payments: external_payments.AsyncExternalPayments
    management_operations: management_operations.AsyncManagementOperations
    with_raw_response: AsyncLithicWithRawResponse
    with_streaming_response: AsyncLithicWithStreamedResponse

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

        self.accounts = accounts.AsyncAccounts(self)
        self.account_holders = account_holders.AsyncAccountHolders(self)
        self.auth_rules = auth_rules.AsyncAuthRules(self)
        self.auth_stream_enrollment = auth_stream_enrollment.AsyncAuthStreamEnrollment(self)
        self.tokenization_decisioning = tokenization_decisioning.AsyncTokenizationDecisioning(self)
        self.tokenizations = tokenizations.AsyncTokenizations(self)
        self.cards = cards.AsyncCards(self)
        self.balances = balances.AsyncBalances(self)
        self.aggregate_balances = aggregate_balances.AsyncAggregateBalances(self)
        self.disputes = disputes.AsyncDisputes(self)
        self.events = events.AsyncEvents(self)
        self.financial_accounts = financial_accounts.AsyncFinancialAccounts(self)
        self.transactions = transactions.AsyncTransactions(self)
        self.responder_endpoints = responder_endpoints.AsyncResponderEndpoints(self)
        self.webhooks = webhooks.AsyncWebhooks(self)
        self.external_bank_accounts = external_bank_accounts.AsyncExternalBankAccounts(self)
        self.payments = payments.AsyncPayments(self)
        self.three_ds = three_ds.AsyncThreeDS(self)
        self.reports = reports.AsyncReports(self)
        self.card_programs = card_programs.AsyncCardPrograms(self)
        self.digital_card_art = digital_card_art.AsyncDigitalCardArtResource(self)
        self.book_transfers = book_transfers.AsyncBookTransfers(self)
        self.credit_products = credit_products.AsyncCreditProducts(self)
        self.external_payments = external_payments.AsyncExternalPayments(self)
        self.management_operations = management_operations.AsyncManagementOperations(self)
        self.with_raw_response = AsyncLithicWithRawResponse(self)
        self.with_streaming_response = AsyncLithicWithStreamedResponse(self)

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
    def __init__(self, client: Lithic) -> None:
        self.accounts = accounts.AccountsWithRawResponse(client.accounts)
        self.account_holders = account_holders.AccountHoldersWithRawResponse(client.account_holders)
        self.auth_rules = auth_rules.AuthRulesWithRawResponse(client.auth_rules)
        self.auth_stream_enrollment = auth_stream_enrollment.AuthStreamEnrollmentWithRawResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = tokenization_decisioning.TokenizationDecisioningWithRawResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = tokenizations.TokenizationsWithRawResponse(client.tokenizations)
        self.cards = cards.CardsWithRawResponse(client.cards)
        self.balances = balances.BalancesWithRawResponse(client.balances)
        self.aggregate_balances = aggregate_balances.AggregateBalancesWithRawResponse(client.aggregate_balances)
        self.disputes = disputes.DisputesWithRawResponse(client.disputes)
        self.events = events.EventsWithRawResponse(client.events)
        self.financial_accounts = financial_accounts.FinancialAccountsWithRawResponse(client.financial_accounts)
        self.transactions = transactions.TransactionsWithRawResponse(client.transactions)
        self.responder_endpoints = responder_endpoints.ResponderEndpointsWithRawResponse(client.responder_endpoints)
        self.external_bank_accounts = external_bank_accounts.ExternalBankAccountsWithRawResponse(
            client.external_bank_accounts
        )
        self.payments = payments.PaymentsWithRawResponse(client.payments)
        self.three_ds = three_ds.ThreeDSWithRawResponse(client.three_ds)
        self.reports = reports.ReportsWithRawResponse(client.reports)
        self.card_programs = card_programs.CardProgramsWithRawResponse(client.card_programs)
        self.digital_card_art = digital_card_art.DigitalCardArtResourceWithRawResponse(client.digital_card_art)
        self.book_transfers = book_transfers.BookTransfersWithRawResponse(client.book_transfers)
        self.credit_products = credit_products.CreditProductsWithRawResponse(client.credit_products)
        self.external_payments = external_payments.ExternalPaymentsWithRawResponse(client.external_payments)
        self.management_operations = management_operations.ManagementOperationsWithRawResponse(
            client.management_operations
        )

        self.api_status = _legacy_response.to_raw_response_wrapper(
            client.api_status,
        )


class AsyncLithicWithRawResponse:
    def __init__(self, client: AsyncLithic) -> None:
        self.accounts = accounts.AsyncAccountsWithRawResponse(client.accounts)
        self.account_holders = account_holders.AsyncAccountHoldersWithRawResponse(client.account_holders)
        self.auth_rules = auth_rules.AsyncAuthRulesWithRawResponse(client.auth_rules)
        self.auth_stream_enrollment = auth_stream_enrollment.AsyncAuthStreamEnrollmentWithRawResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = tokenization_decisioning.AsyncTokenizationDecisioningWithRawResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = tokenizations.AsyncTokenizationsWithRawResponse(client.tokenizations)
        self.cards = cards.AsyncCardsWithRawResponse(client.cards)
        self.balances = balances.AsyncBalancesWithRawResponse(client.balances)
        self.aggregate_balances = aggregate_balances.AsyncAggregateBalancesWithRawResponse(client.aggregate_balances)
        self.disputes = disputes.AsyncDisputesWithRawResponse(client.disputes)
        self.events = events.AsyncEventsWithRawResponse(client.events)
        self.financial_accounts = financial_accounts.AsyncFinancialAccountsWithRawResponse(client.financial_accounts)
        self.transactions = transactions.AsyncTransactionsWithRawResponse(client.transactions)
        self.responder_endpoints = responder_endpoints.AsyncResponderEndpointsWithRawResponse(
            client.responder_endpoints
        )
        self.external_bank_accounts = external_bank_accounts.AsyncExternalBankAccountsWithRawResponse(
            client.external_bank_accounts
        )
        self.payments = payments.AsyncPaymentsWithRawResponse(client.payments)
        self.three_ds = three_ds.AsyncThreeDSWithRawResponse(client.three_ds)
        self.reports = reports.AsyncReportsWithRawResponse(client.reports)
        self.card_programs = card_programs.AsyncCardProgramsWithRawResponse(client.card_programs)
        self.digital_card_art = digital_card_art.AsyncDigitalCardArtResourceWithRawResponse(client.digital_card_art)
        self.book_transfers = book_transfers.AsyncBookTransfersWithRawResponse(client.book_transfers)
        self.credit_products = credit_products.AsyncCreditProductsWithRawResponse(client.credit_products)
        self.external_payments = external_payments.AsyncExternalPaymentsWithRawResponse(client.external_payments)
        self.management_operations = management_operations.AsyncManagementOperationsWithRawResponse(
            client.management_operations
        )

        self.api_status = _legacy_response.async_to_raw_response_wrapper(
            client.api_status,
        )


class LithicWithStreamedResponse:
    def __init__(self, client: Lithic) -> None:
        self.accounts = accounts.AccountsWithStreamingResponse(client.accounts)
        self.account_holders = account_holders.AccountHoldersWithStreamingResponse(client.account_holders)
        self.auth_rules = auth_rules.AuthRulesWithStreamingResponse(client.auth_rules)
        self.auth_stream_enrollment = auth_stream_enrollment.AuthStreamEnrollmentWithStreamingResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = tokenization_decisioning.TokenizationDecisioningWithStreamingResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = tokenizations.TokenizationsWithStreamingResponse(client.tokenizations)
        self.cards = cards.CardsWithStreamingResponse(client.cards)
        self.balances = balances.BalancesWithStreamingResponse(client.balances)
        self.aggregate_balances = aggregate_balances.AggregateBalancesWithStreamingResponse(client.aggregate_balances)
        self.disputes = disputes.DisputesWithStreamingResponse(client.disputes)
        self.events = events.EventsWithStreamingResponse(client.events)
        self.financial_accounts = financial_accounts.FinancialAccountsWithStreamingResponse(client.financial_accounts)
        self.transactions = transactions.TransactionsWithStreamingResponse(client.transactions)
        self.responder_endpoints = responder_endpoints.ResponderEndpointsWithStreamingResponse(
            client.responder_endpoints
        )
        self.external_bank_accounts = external_bank_accounts.ExternalBankAccountsWithStreamingResponse(
            client.external_bank_accounts
        )
        self.payments = payments.PaymentsWithStreamingResponse(client.payments)
        self.three_ds = three_ds.ThreeDSWithStreamingResponse(client.three_ds)
        self.reports = reports.ReportsWithStreamingResponse(client.reports)
        self.card_programs = card_programs.CardProgramsWithStreamingResponse(client.card_programs)
        self.digital_card_art = digital_card_art.DigitalCardArtResourceWithStreamingResponse(client.digital_card_art)
        self.book_transfers = book_transfers.BookTransfersWithStreamingResponse(client.book_transfers)
        self.credit_products = credit_products.CreditProductsWithStreamingResponse(client.credit_products)
        self.external_payments = external_payments.ExternalPaymentsWithStreamingResponse(client.external_payments)
        self.management_operations = management_operations.ManagementOperationsWithStreamingResponse(
            client.management_operations
        )

        self.api_status = to_streamed_response_wrapper(
            client.api_status,
        )


class AsyncLithicWithStreamedResponse:
    def __init__(self, client: AsyncLithic) -> None:
        self.accounts = accounts.AsyncAccountsWithStreamingResponse(client.accounts)
        self.account_holders = account_holders.AsyncAccountHoldersWithStreamingResponse(client.account_holders)
        self.auth_rules = auth_rules.AsyncAuthRulesWithStreamingResponse(client.auth_rules)
        self.auth_stream_enrollment = auth_stream_enrollment.AsyncAuthStreamEnrollmentWithStreamingResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = tokenization_decisioning.AsyncTokenizationDecisioningWithStreamingResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = tokenizations.AsyncTokenizationsWithStreamingResponse(client.tokenizations)
        self.cards = cards.AsyncCardsWithStreamingResponse(client.cards)
        self.balances = balances.AsyncBalancesWithStreamingResponse(client.balances)
        self.aggregate_balances = aggregate_balances.AsyncAggregateBalancesWithStreamingResponse(
            client.aggregate_balances
        )
        self.disputes = disputes.AsyncDisputesWithStreamingResponse(client.disputes)
        self.events = events.AsyncEventsWithStreamingResponse(client.events)
        self.financial_accounts = financial_accounts.AsyncFinancialAccountsWithStreamingResponse(
            client.financial_accounts
        )
        self.transactions = transactions.AsyncTransactionsWithStreamingResponse(client.transactions)
        self.responder_endpoints = responder_endpoints.AsyncResponderEndpointsWithStreamingResponse(
            client.responder_endpoints
        )
        self.external_bank_accounts = external_bank_accounts.AsyncExternalBankAccountsWithStreamingResponse(
            client.external_bank_accounts
        )
        self.payments = payments.AsyncPaymentsWithStreamingResponse(client.payments)
        self.three_ds = three_ds.AsyncThreeDSWithStreamingResponse(client.three_ds)
        self.reports = reports.AsyncReportsWithStreamingResponse(client.reports)
        self.card_programs = card_programs.AsyncCardProgramsWithStreamingResponse(client.card_programs)
        self.digital_card_art = digital_card_art.AsyncDigitalCardArtResourceWithStreamingResponse(
            client.digital_card_art
        )
        self.book_transfers = book_transfers.AsyncBookTransfersWithStreamingResponse(client.book_transfers)
        self.credit_products = credit_products.AsyncCreditProductsWithStreamingResponse(client.credit_products)
        self.external_payments = external_payments.AsyncExternalPaymentsWithStreamingResponse(client.external_payments)
        self.management_operations = management_operations.AsyncManagementOperationsWithStreamingResponse(
            client.management_operations
        )

        self.api_status = async_to_streamed_response_wrapper(
            client.api_status,
        )


Client = Lithic

AsyncClient = AsyncLithic
