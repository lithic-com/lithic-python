# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions, _legacy_response
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
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LithicError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.api_status import APIStatus

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
    accounts: resources.AccountsResource
    account_holders: resources.AccountHoldersResource
    auth_rules: resources.AuthRulesResource
    auth_stream_enrollment: resources.AuthStreamEnrollmentResource
    tokenization_decisioning: resources.TokenizationDecisioningResource
    tokenizations: resources.TokenizationsResource
    cards: resources.CardsResource
    balances: resources.BalancesResource
    aggregate_balances: resources.AggregateBalancesResource
    disputes: resources.DisputesResource
    events: resources.EventsResource
    financial_accounts: resources.FinancialAccountsResource
    transactions: resources.TransactionsResource
    responder_endpoints: resources.ResponderEndpointsResource
    webhooks: resources.WebhooksResource
    external_bank_accounts: resources.ExternalBankAccountsResource
    payments: resources.PaymentsResource
    three_ds: resources.ThreeDSResource
    reports: resources.ReportsResource
    card_product: resources.CardProductResource
    card_programs: resources.CardProgramsResource
    digital_card_art: resources.DigitalCardArtResource
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
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.AccountsResource(self)
        self.account_holders = resources.AccountHoldersResource(self)
        self.auth_rules = resources.AuthRulesResource(self)
        self.auth_stream_enrollment = resources.AuthStreamEnrollmentResource(self)
        self.tokenization_decisioning = resources.TokenizationDecisioningResource(self)
        self.tokenizations = resources.TokenizationsResource(self)
        self.cards = resources.CardsResource(self)
        self.balances = resources.BalancesResource(self)
        self.aggregate_balances = resources.AggregateBalancesResource(self)
        self.disputes = resources.DisputesResource(self)
        self.events = resources.EventsResource(self)
        self.financial_accounts = resources.FinancialAccountsResource(self)
        self.transactions = resources.TransactionsResource(self)
        self.responder_endpoints = resources.ResponderEndpointsResource(self)
        self.webhooks = resources.WebhooksResource(self)
        self.external_bank_accounts = resources.ExternalBankAccountsResource(self)
        self.payments = resources.PaymentsResource(self)
        self.three_ds = resources.ThreeDSResource(self)
        self.reports = resources.ReportsResource(self)
        self.card_product = resources.CardProductResource(self)
        self.card_programs = resources.CardProgramsResource(self)
        self.digital_card_art = resources.DigitalCardArtResource(self)
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
    accounts: resources.AsyncAccountsResource
    account_holders: resources.AsyncAccountHoldersResource
    auth_rules: resources.AsyncAuthRulesResource
    auth_stream_enrollment: resources.AsyncAuthStreamEnrollmentResource
    tokenization_decisioning: resources.AsyncTokenizationDecisioningResource
    tokenizations: resources.AsyncTokenizationsResource
    cards: resources.AsyncCardsResource
    balances: resources.AsyncBalancesResource
    aggregate_balances: resources.AsyncAggregateBalancesResource
    disputes: resources.AsyncDisputesResource
    events: resources.AsyncEventsResource
    financial_accounts: resources.AsyncFinancialAccountsResource
    transactions: resources.AsyncTransactionsResource
    responder_endpoints: resources.AsyncResponderEndpointsResource
    webhooks: resources.AsyncWebhooksResource
    external_bank_accounts: resources.AsyncExternalBankAccountsResource
    payments: resources.AsyncPaymentsResource
    three_ds: resources.AsyncThreeDSResource
    reports: resources.AsyncReportsResource
    card_product: resources.AsyncCardProductResource
    card_programs: resources.AsyncCardProgramsResource
    digital_card_art: resources.AsyncDigitalCardArtResource
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
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.AsyncAccountsResource(self)
        self.account_holders = resources.AsyncAccountHoldersResource(self)
        self.auth_rules = resources.AsyncAuthRulesResource(self)
        self.auth_stream_enrollment = resources.AsyncAuthStreamEnrollmentResource(self)
        self.tokenization_decisioning = resources.AsyncTokenizationDecisioningResource(self)
        self.tokenizations = resources.AsyncTokenizationsResource(self)
        self.cards = resources.AsyncCardsResource(self)
        self.balances = resources.AsyncBalancesResource(self)
        self.aggregate_balances = resources.AsyncAggregateBalancesResource(self)
        self.disputes = resources.AsyncDisputesResource(self)
        self.events = resources.AsyncEventsResource(self)
        self.financial_accounts = resources.AsyncFinancialAccountsResource(self)
        self.transactions = resources.AsyncTransactionsResource(self)
        self.responder_endpoints = resources.AsyncResponderEndpointsResource(self)
        self.webhooks = resources.AsyncWebhooksResource(self)
        self.external_bank_accounts = resources.AsyncExternalBankAccountsResource(self)
        self.payments = resources.AsyncPaymentsResource(self)
        self.three_ds = resources.AsyncThreeDSResource(self)
        self.reports = resources.AsyncReportsResource(self)
        self.card_product = resources.AsyncCardProductResource(self)
        self.card_programs = resources.AsyncCardProgramsResource(self)
        self.digital_card_art = resources.AsyncDigitalCardArtResource(self)
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
        self.accounts = resources.AccountsResourceWithRawResponse(client.accounts)
        self.account_holders = resources.AccountHoldersResourceWithRawResponse(client.account_holders)
        self.auth_rules = resources.AuthRulesResourceWithRawResponse(client.auth_rules)
        self.auth_stream_enrollment = resources.AuthStreamEnrollmentResourceWithRawResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = resources.TokenizationDecisioningResourceWithRawResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = resources.TokenizationsResourceWithRawResponse(client.tokenizations)
        self.cards = resources.CardsResourceWithRawResponse(client.cards)
        self.balances = resources.BalancesResourceWithRawResponse(client.balances)
        self.aggregate_balances = resources.AggregateBalancesResourceWithRawResponse(client.aggregate_balances)
        self.disputes = resources.DisputesResourceWithRawResponse(client.disputes)
        self.events = resources.EventsResourceWithRawResponse(client.events)
        self.financial_accounts = resources.FinancialAccountsResourceWithRawResponse(client.financial_accounts)
        self.transactions = resources.TransactionsResourceWithRawResponse(client.transactions)
        self.responder_endpoints = resources.ResponderEndpointsResourceWithRawResponse(client.responder_endpoints)
        self.external_bank_accounts = resources.ExternalBankAccountsResourceWithRawResponse(
            client.external_bank_accounts
        )
        self.payments = resources.PaymentsResourceWithRawResponse(client.payments)
        self.three_ds = resources.ThreeDSResourceWithRawResponse(client.three_ds)
        self.reports = resources.ReportsResourceWithRawResponse(client.reports)
        self.card_product = resources.CardProductResourceWithRawResponse(client.card_product)
        self.card_programs = resources.CardProgramsResourceWithRawResponse(client.card_programs)
        self.digital_card_art = resources.DigitalCardArtResourceWithRawResponse(client.digital_card_art)

        self.api_status = _legacy_response.to_raw_response_wrapper(
            client.api_status,
        )


class AsyncLithicWithRawResponse:
    def __init__(self, client: AsyncLithic) -> None:
        self.accounts = resources.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.account_holders = resources.AsyncAccountHoldersResourceWithRawResponse(client.account_holders)
        self.auth_rules = resources.AsyncAuthRulesResourceWithRawResponse(client.auth_rules)
        self.auth_stream_enrollment = resources.AsyncAuthStreamEnrollmentResourceWithRawResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = resources.AsyncTokenizationDecisioningResourceWithRawResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = resources.AsyncTokenizationsResourceWithRawResponse(client.tokenizations)
        self.cards = resources.AsyncCardsResourceWithRawResponse(client.cards)
        self.balances = resources.AsyncBalancesResourceWithRawResponse(client.balances)
        self.aggregate_balances = resources.AsyncAggregateBalancesResourceWithRawResponse(client.aggregate_balances)
        self.disputes = resources.AsyncDisputesResourceWithRawResponse(client.disputes)
        self.events = resources.AsyncEventsResourceWithRawResponse(client.events)
        self.financial_accounts = resources.AsyncFinancialAccountsResourceWithRawResponse(client.financial_accounts)
        self.transactions = resources.AsyncTransactionsResourceWithRawResponse(client.transactions)
        self.responder_endpoints = resources.AsyncResponderEndpointsResourceWithRawResponse(client.responder_endpoints)
        self.external_bank_accounts = resources.AsyncExternalBankAccountsResourceWithRawResponse(
            client.external_bank_accounts
        )
        self.payments = resources.AsyncPaymentsResourceWithRawResponse(client.payments)
        self.three_ds = resources.AsyncThreeDSResourceWithRawResponse(client.three_ds)
        self.reports = resources.AsyncReportsResourceWithRawResponse(client.reports)
        self.card_product = resources.AsyncCardProductResourceWithRawResponse(client.card_product)
        self.card_programs = resources.AsyncCardProgramsResourceWithRawResponse(client.card_programs)
        self.digital_card_art = resources.AsyncDigitalCardArtResourceWithRawResponse(client.digital_card_art)

        self.api_status = _legacy_response.async_to_raw_response_wrapper(
            client.api_status,
        )


class LithicWithStreamedResponse:
    def __init__(self, client: Lithic) -> None:
        self.accounts = resources.AccountsResourceWithStreamingResponse(client.accounts)
        self.account_holders = resources.AccountHoldersResourceWithStreamingResponse(client.account_holders)
        self.auth_rules = resources.AuthRulesResourceWithStreamingResponse(client.auth_rules)
        self.auth_stream_enrollment = resources.AuthStreamEnrollmentResourceWithStreamingResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = resources.TokenizationDecisioningResourceWithStreamingResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = resources.TokenizationsResourceWithStreamingResponse(client.tokenizations)
        self.cards = resources.CardsResourceWithStreamingResponse(client.cards)
        self.balances = resources.BalancesResourceWithStreamingResponse(client.balances)
        self.aggregate_balances = resources.AggregateBalancesResourceWithStreamingResponse(client.aggregate_balances)
        self.disputes = resources.DisputesResourceWithStreamingResponse(client.disputes)
        self.events = resources.EventsResourceWithStreamingResponse(client.events)
        self.financial_accounts = resources.FinancialAccountsResourceWithStreamingResponse(client.financial_accounts)
        self.transactions = resources.TransactionsResourceWithStreamingResponse(client.transactions)
        self.responder_endpoints = resources.ResponderEndpointsResourceWithStreamingResponse(client.responder_endpoints)
        self.external_bank_accounts = resources.ExternalBankAccountsResourceWithStreamingResponse(
            client.external_bank_accounts
        )
        self.payments = resources.PaymentsResourceWithStreamingResponse(client.payments)
        self.three_ds = resources.ThreeDSResourceWithStreamingResponse(client.three_ds)
        self.reports = resources.ReportsResourceWithStreamingResponse(client.reports)
        self.card_product = resources.CardProductResourceWithStreamingResponse(client.card_product)
        self.card_programs = resources.CardProgramsResourceWithStreamingResponse(client.card_programs)
        self.digital_card_art = resources.DigitalCardArtResourceWithStreamingResponse(client.digital_card_art)

        self.api_status = to_streamed_response_wrapper(
            client.api_status,
        )


class AsyncLithicWithStreamedResponse:
    def __init__(self, client: AsyncLithic) -> None:
        self.accounts = resources.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.account_holders = resources.AsyncAccountHoldersResourceWithStreamingResponse(client.account_holders)
        self.auth_rules = resources.AsyncAuthRulesResourceWithStreamingResponse(client.auth_rules)
        self.auth_stream_enrollment = resources.AsyncAuthStreamEnrollmentResourceWithStreamingResponse(
            client.auth_stream_enrollment
        )
        self.tokenization_decisioning = resources.AsyncTokenizationDecisioningResourceWithStreamingResponse(
            client.tokenization_decisioning
        )
        self.tokenizations = resources.AsyncTokenizationsResourceWithStreamingResponse(client.tokenizations)
        self.cards = resources.AsyncCardsResourceWithStreamingResponse(client.cards)
        self.balances = resources.AsyncBalancesResourceWithStreamingResponse(client.balances)
        self.aggregate_balances = resources.AsyncAggregateBalancesResourceWithStreamingResponse(
            client.aggregate_balances
        )
        self.disputes = resources.AsyncDisputesResourceWithStreamingResponse(client.disputes)
        self.events = resources.AsyncEventsResourceWithStreamingResponse(client.events)
        self.financial_accounts = resources.AsyncFinancialAccountsResourceWithStreamingResponse(
            client.financial_accounts
        )
        self.transactions = resources.AsyncTransactionsResourceWithStreamingResponse(client.transactions)
        self.responder_endpoints = resources.AsyncResponderEndpointsResourceWithStreamingResponse(
            client.responder_endpoints
        )
        self.external_bank_accounts = resources.AsyncExternalBankAccountsResourceWithStreamingResponse(
            client.external_bank_accounts
        )
        self.payments = resources.AsyncPaymentsResourceWithStreamingResponse(client.payments)
        self.three_ds = resources.AsyncThreeDSResourceWithStreamingResponse(client.three_ds)
        self.reports = resources.AsyncReportsResourceWithStreamingResponse(client.reports)
        self.card_product = resources.AsyncCardProductResourceWithStreamingResponse(client.card_product)
        self.card_programs = resources.AsyncCardProgramsResourceWithStreamingResponse(client.card_programs)
        self.digital_card_art = resources.AsyncDigitalCardArtResourceWithStreamingResponse(client.digital_card_art)

        self.api_status = async_to_streamed_response_wrapper(
            client.api_status,
        )


Client = Lithic

AsyncClient = AsyncLithic
