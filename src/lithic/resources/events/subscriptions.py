# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.events import (
    subscription_list_params,
    subscription_create_params,
    subscription_update_params,
    subscription_recover_params,
    subscription_list_attempts_params,
    subscription_replay_missing_params,
    subscription_send_simulated_example_params,
)
from ...types.message_attempt import MessageAttempt
from ...types.event_subscription import EventSubscription
from ...types.events.subscription_retrieve_secret_response import SubscriptionRetrieveSecretResponse

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return SubscriptionsWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "auth_rules.performance_report.created",
                "balance.updated",
                "book_transfer_transaction.created",
                "card.created",
                "card.renewed",
                "card.reissued",
                "card.converted",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "digital_wallet.tokenization_two_factor_authentication_code_sent",
                "digital_wallet.tokenization_updated",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "external_bank_account.created",
                "external_bank_account.updated",
                "external_payment.created",
                "external_payment.updated",
                "financial_account.created",
                "financial_account.updated",
                "loan_tape.created",
                "loan_tape.updated",
                "management_operation.created",
                "management_operation.updated",
                "payment_transaction.created",
                "payment_transaction.updated",
                "internal_transaction.created",
                "internal_transaction.updated",
                "settlement_report.updated",
                "statements.created",
                "three_ds_authentication.created",
                "three_ds_authentication.updated",
                "tokenization.approval_request",
                "tokenization.result",
                "tokenization.two_factor_authentication_code",
                "tokenization.two_factor_authentication_code_sent",
                "tokenization.updated",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Create a new event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/event_subscriptions",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def retrieve(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Get an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._get(
            f"/v1/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def update(
        self,
        event_subscription_token: str,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "auth_rules.performance_report.created",
                "balance.updated",
                "book_transfer_transaction.created",
                "card.created",
                "card.renewed",
                "card.reissued",
                "card.converted",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "digital_wallet.tokenization_two_factor_authentication_code_sent",
                "digital_wallet.tokenization_updated",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "external_bank_account.created",
                "external_bank_account.updated",
                "external_payment.created",
                "external_payment.updated",
                "financial_account.created",
                "financial_account.updated",
                "loan_tape.created",
                "loan_tape.updated",
                "management_operation.created",
                "management_operation.updated",
                "payment_transaction.created",
                "payment_transaction.updated",
                "internal_transaction.created",
                "internal_transaction.updated",
                "settlement_report.updated",
                "statements.created",
                "three_ds_authentication.created",
                "three_ds_authentication.updated",
                "tokenization.approval_request",
                "tokenization.result",
                "tokenization.two_factor_authentication_code",
                "tokenization.two_factor_authentication_code_sent",
                "tokenization.updated",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Update an event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._patch(
            f"/v1/event_subscriptions/{event_subscription_token}",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[EventSubscription]:
        """
        List all the event subscriptions.

        Args:
          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/event_subscriptions",
            page=SyncCursorPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )

    def delete(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._delete(
            f"/v1/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_attempts(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["FAILED", "PENDING", "SENDING", "SUCCESS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[MessageAttempt]:
        """
        List all the message attempts for a given event subscription.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._get_api_list(
            f"/v1/event_subscriptions/{event_subscription_token}/attempts",
            page=SyncCursorPage[MessageAttempt],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    subscription_list_attempts_params.SubscriptionListAttemptsParams,
                ),
            ),
            model=MessageAttempt,
        )

    def recover(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resend all failed messages since a given time.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._post(
            f"/v1/event_subscriptions/{event_subscription_token}/recover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_recover_params.SubscriptionRecoverParams,
                ),
            ),
            cast_to=NoneType,
        )

    def replay_missing(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Replays messages to the endpoint.

        Only messages that were created after `begin`
        will be sent. Messages that were previously sent to the endpoint are not resent.
        Message will be retried if endpoint responds with a non-2xx status code. See
        [Retry Schedule](https://docs.lithic.com/docs/events-api#retry-schedule) for
        details.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._post(
            f"/v1/event_subscriptions/{event_subscription_token}/replay_missing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_replay_missing_params.SubscriptionReplayMissingParams,
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionRetrieveSecretResponse:
        """
        Get the secret for an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._get(
            f"/v1/event_subscriptions/{event_subscription_token}/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveSecretResponse,
        )

    def rotate_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Rotate the secret for an event subscription.

        The previous secret will be valid
        for the next 24 hours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._post(
            f"/v1/event_subscriptions/{event_subscription_token}/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_simulated_example(
        self,
        event_subscription_token: str,
        *,
        event_type: Literal[
            "account_holder.created",
            "account_holder.updated",
            "account_holder.verification",
            "auth_rules.performance_report.created",
            "balance.updated",
            "book_transfer_transaction.created",
            "card.created",
            "card.renewed",
            "card.reissued",
            "card.converted",
            "card.shipped",
            "card_transaction.updated",
            "digital_wallet.tokenization_approval_request",
            "digital_wallet.tokenization_result",
            "digital_wallet.tokenization_two_factor_authentication_code",
            "digital_wallet.tokenization_two_factor_authentication_code_sent",
            "digital_wallet.tokenization_updated",
            "dispute.updated",
            "dispute_evidence.upload_failed",
            "external_bank_account.created",
            "external_bank_account.updated",
            "external_payment.created",
            "external_payment.updated",
            "financial_account.created",
            "financial_account.updated",
            "loan_tape.created",
            "loan_tape.updated",
            "management_operation.created",
            "management_operation.updated",
            "payment_transaction.created",
            "payment_transaction.updated",
            "internal_transaction.created",
            "internal_transaction.updated",
            "settlement_report.updated",
            "statements.created",
            "three_ds_authentication.created",
            "three_ds_authentication.updated",
            "tokenization.approval_request",
            "tokenization.result",
            "tokenization.two_factor_authentication_code",
            "tokenization.two_factor_authentication_code_sent",
            "tokenization.updated",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send an example message for event.

        Args:
          event_type: Event type to send example message for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._post(
            f"/v1/simulate/event_subscriptions/{event_subscription_token}/send_example",
            body=maybe_transform(
                {"event_type": event_type},
                subscription_send_simulated_example_params.SubscriptionSendSimulatedExampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSubscriptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncSubscriptionsWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "auth_rules.performance_report.created",
                "balance.updated",
                "book_transfer_transaction.created",
                "card.created",
                "card.renewed",
                "card.reissued",
                "card.converted",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "digital_wallet.tokenization_two_factor_authentication_code_sent",
                "digital_wallet.tokenization_updated",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "external_bank_account.created",
                "external_bank_account.updated",
                "external_payment.created",
                "external_payment.updated",
                "financial_account.created",
                "financial_account.updated",
                "loan_tape.created",
                "loan_tape.updated",
                "management_operation.created",
                "management_operation.updated",
                "payment_transaction.created",
                "payment_transaction.updated",
                "internal_transaction.created",
                "internal_transaction.updated",
                "settlement_report.updated",
                "statements.created",
                "three_ds_authentication.created",
                "three_ds_authentication.updated",
                "tokenization.approval_request",
                "tokenization.result",
                "tokenization.two_factor_authentication_code",
                "tokenization.two_factor_authentication_code_sent",
                "tokenization.updated",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Create a new event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/event_subscriptions",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    async def retrieve(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Get an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._get(
            f"/v1/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    async def update(
        self,
        event_subscription_token: str,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "auth_rules.performance_report.created",
                "balance.updated",
                "book_transfer_transaction.created",
                "card.created",
                "card.renewed",
                "card.reissued",
                "card.converted",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "digital_wallet.tokenization_two_factor_authentication_code_sent",
                "digital_wallet.tokenization_updated",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "external_bank_account.created",
                "external_bank_account.updated",
                "external_payment.created",
                "external_payment.updated",
                "financial_account.created",
                "financial_account.updated",
                "loan_tape.created",
                "loan_tape.updated",
                "management_operation.created",
                "management_operation.updated",
                "payment_transaction.created",
                "payment_transaction.updated",
                "internal_transaction.created",
                "internal_transaction.updated",
                "settlement_report.updated",
                "statements.created",
                "three_ds_authentication.created",
                "three_ds_authentication.updated",
                "tokenization.approval_request",
                "tokenization.result",
                "tokenization.two_factor_authentication_code",
                "tokenization.two_factor_authentication_code_sent",
                "tokenization.updated",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Update an event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._patch(
            f"/v1/event_subscriptions/{event_subscription_token}",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EventSubscription, AsyncCursorPage[EventSubscription]]:
        """
        List all the event subscriptions.

        Args:
          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/event_subscriptions",
            page=AsyncCursorPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )

    async def delete(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._delete(
            f"/v1/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_attempts(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["FAILED", "PENDING", "SENDING", "SUCCESS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MessageAttempt, AsyncCursorPage[MessageAttempt]]:
        """
        List all the message attempts for a given event subscription.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._get_api_list(
            f"/v1/event_subscriptions/{event_subscription_token}/attempts",
            page=AsyncCursorPage[MessageAttempt],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    subscription_list_attempts_params.SubscriptionListAttemptsParams,
                ),
            ),
            model=MessageAttempt,
        )

    async def recover(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resend all failed messages since a given time.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._post(
            f"/v1/event_subscriptions/{event_subscription_token}/recover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_recover_params.SubscriptionRecoverParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def replay_missing(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Replays messages to the endpoint.

        Only messages that were created after `begin`
        will be sent. Messages that were previously sent to the endpoint are not resent.
        Message will be retried if endpoint responds with a non-2xx status code. See
        [Retry Schedule](https://docs.lithic.com/docs/events-api#retry-schedule) for
        details.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._post(
            f"/v1/event_subscriptions/{event_subscription_token}/replay_missing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_replay_missing_params.SubscriptionReplayMissingParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionRetrieveSecretResponse:
        """
        Get the secret for an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._get(
            f"/v1/event_subscriptions/{event_subscription_token}/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveSecretResponse,
        )

    async def rotate_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Rotate the secret for an event subscription.

        The previous secret will be valid
        for the next 24 hours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._post(
            f"/v1/event_subscriptions/{event_subscription_token}/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_simulated_example(
        self,
        event_subscription_token: str,
        *,
        event_type: Literal[
            "account_holder.created",
            "account_holder.updated",
            "account_holder.verification",
            "auth_rules.performance_report.created",
            "balance.updated",
            "book_transfer_transaction.created",
            "card.created",
            "card.renewed",
            "card.reissued",
            "card.converted",
            "card.shipped",
            "card_transaction.updated",
            "digital_wallet.tokenization_approval_request",
            "digital_wallet.tokenization_result",
            "digital_wallet.tokenization_two_factor_authentication_code",
            "digital_wallet.tokenization_two_factor_authentication_code_sent",
            "digital_wallet.tokenization_updated",
            "dispute.updated",
            "dispute_evidence.upload_failed",
            "external_bank_account.created",
            "external_bank_account.updated",
            "external_payment.created",
            "external_payment.updated",
            "financial_account.created",
            "financial_account.updated",
            "loan_tape.created",
            "loan_tape.updated",
            "management_operation.created",
            "management_operation.updated",
            "payment_transaction.created",
            "payment_transaction.updated",
            "internal_transaction.created",
            "internal_transaction.updated",
            "settlement_report.updated",
            "statements.created",
            "three_ds_authentication.created",
            "three_ds_authentication.updated",
            "tokenization.approval_request",
            "tokenization.result",
            "tokenization.two_factor_authentication_code",
            "tokenization.two_factor_authentication_code_sent",
            "tokenization.updated",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send an example message for event.

        Args:
          event_type: Event type to send example message for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._post(
            f"/v1/simulate/event_subscriptions/{event_subscription_token}/send_example",
            body=await async_maybe_transform(
                {"event_type": event_type},
                subscription_send_simulated_example_params.SubscriptionSendSimulatedExampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = _legacy_response.to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.list_attempts = _legacy_response.to_raw_response_wrapper(
            subscriptions.list_attempts,
        )
        self.recover = _legacy_response.to_raw_response_wrapper(
            subscriptions.recover,
        )
        self.replay_missing = _legacy_response.to_raw_response_wrapper(
            subscriptions.replay_missing,
        )
        self.retrieve_secret = _legacy_response.to_raw_response_wrapper(
            subscriptions.retrieve_secret,
        )
        self.rotate_secret = _legacy_response.to_raw_response_wrapper(
            subscriptions.rotate_secret,
        )
        self.send_simulated_example = _legacy_response.to_raw_response_wrapper(
            subscriptions.send_simulated_example,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.list_attempts = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.list_attempts,
        )
        self.recover = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.recover,
        )
        self.replay_missing = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.replay_missing,
        )
        self.retrieve_secret = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.retrieve_secret,
        )
        self.rotate_secret = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.rotate_secret,
        )
        self.send_simulated_example = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.send_simulated_example,
        )


class SubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.list_attempts = to_streamed_response_wrapper(
            subscriptions.list_attempts,
        )
        self.recover = to_streamed_response_wrapper(
            subscriptions.recover,
        )
        self.replay_missing = to_streamed_response_wrapper(
            subscriptions.replay_missing,
        )
        self.retrieve_secret = to_streamed_response_wrapper(
            subscriptions.retrieve_secret,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            subscriptions.rotate_secret,
        )
        self.send_simulated_example = to_streamed_response_wrapper(
            subscriptions.send_simulated_example,
        )


class AsyncSubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.list_attempts = async_to_streamed_response_wrapper(
            subscriptions.list_attempts,
        )
        self.recover = async_to_streamed_response_wrapper(
            subscriptions.recover,
        )
        self.replay_missing = async_to_streamed_response_wrapper(
            subscriptions.replay_missing,
        )
        self.retrieve_secret = async_to_streamed_response_wrapper(
            subscriptions.retrieve_secret,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            subscriptions.rotate_secret,
        )
        self.send_simulated_example = async_to_streamed_response_wrapper(
            subscriptions.send_simulated_example,
        )
