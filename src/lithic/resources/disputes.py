# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    dispute_list_params,
    dispute_create_params,
    dispute_update_params,
    dispute_list_evidences_params,
    dispute_initiate_evidence_upload_params,
)
from .._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileTypes,
)
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.dispute import Dispute
from ..types.dispute_evidence import DisputeEvidence

__all__ = ["Disputes", "AsyncDisputes"]


class Disputes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DisputesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return DisputesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisputesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return DisputesWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        reason: Literal[
            "ATM_CASH_MISDISPENSE",
            "CANCELLED",
            "DUPLICATED",
            "FRAUD_CARD_NOT_PRESENT",
            "FRAUD_CARD_PRESENT",
            "FRAUD_OTHER",
            "GOODS_SERVICES_NOT_AS_DESCRIBED",
            "GOODS_SERVICES_NOT_RECEIVED",
            "INCORRECT_AMOUNT",
            "MISSING_AUTH",
            "OTHER",
            "PROCESSING_ERROR",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
            "REFUND_NOT_PROCESSED",
        ],
        transaction_token: str,
        customer_filed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_note: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """
        Initiate a dispute.

        Args:
          amount: Amount to dispute

          reason: Reason for dispute

          transaction_token: Transaction to dispute

          customer_filed_date: Date the customer filed the dispute

          customer_note: Customer description of dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/disputes",
            body=maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                    "transaction_token": transaction_token,
                    "customer_filed_date": customer_filed_date,
                    "customer_note": customer_note,
                },
                dispute_create_params.DisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def retrieve(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """
        Get dispute.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return self._get(
            f"/v1/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def update(
        self,
        dispute_token: str,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        customer_filed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_note: str | NotGiven = NOT_GIVEN,
        reason: Literal[
            "ATM_CASH_MISDISPENSE",
            "CANCELLED",
            "DUPLICATED",
            "FRAUD_CARD_NOT_PRESENT",
            "FRAUD_CARD_PRESENT",
            "FRAUD_OTHER",
            "GOODS_SERVICES_NOT_AS_DESCRIBED",
            "GOODS_SERVICES_NOT_RECEIVED",
            "INCORRECT_AMOUNT",
            "MISSING_AUTH",
            "OTHER",
            "PROCESSING_ERROR",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
            "REFUND_NOT_PROCESSED",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """Update dispute.

        Can only be modified if status is `NEW`.

        Args:
          amount: Amount to dispute

          customer_filed_date: Date the customer filed the dispute

          customer_note: Customer description of dispute

          reason: Reason for dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return self._patch(
            f"/v1/disputes/{dispute_token}",
            body=maybe_transform(
                {
                    "amount": amount,
                    "customer_filed_date": customer_filed_date,
                    "customer_note": customer_note,
                    "reason": reason,
                },
                dispute_update_params.DisputeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "ARBITRATION",
            "CASE_CLOSED",
            "CASE_WON",
            "NEW",
            "PENDING_CUSTOMER",
            "PREARBITRATION",
            "REPRESENTMENT",
            "SUBMITTED",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_tokens: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Dispute]:
        """List disputes.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: List disputes of a specific status.

          transaction_tokens: Transaction tokens to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/disputes",
            page=SyncCursorPage[Dispute],
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
                        "transaction_tokens": transaction_tokens,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=Dispute,
        )

    def delete(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """
        Withdraw dispute.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return self._delete(
            f"/v1/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def delete_evidence(
        self,
        evidence_token: str,
        *,
        dispute_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """Soft delete evidence for a dispute.

        Evidence will not be reviewed or submitted
        by Lithic after it is withdrawn.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        if not evidence_token:
            raise ValueError(f"Expected a non-empty value for `evidence_token` but received {evidence_token!r}")
        return self._delete(
            f"/v1/disputes/{dispute_token}/evidences/{evidence_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeEvidence,
        )

    def initiate_evidence_upload(
        self,
        dispute_token: str,
        *,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """Use this endpoint to upload evidences for the dispute.

        It will return a URL to
        upload your documents to. The URL will expire in 30 minutes.

        Uploaded documents must either be a `jpg`, `png` or `pdf` file, and each must be
        less than 5 GiB.

        Args:
          filename: Filename of the evidence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return self._post(
            f"/v1/disputes/{dispute_token}/evidences",
            body=maybe_transform(
                {"filename": filename}, dispute_initiate_evidence_upload_params.DisputeInitiateEvidenceUploadParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeEvidence,
        )

    def list_evidences(
        self,
        dispute_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[DisputeEvidence]:
        """
        List evidence metadata for a dispute.

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
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return self._get_api_list(
            f"/v1/disputes/{dispute_token}/evidences",
            page=SyncCursorPage[DisputeEvidence],
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
                    },
                    dispute_list_evidences_params.DisputeListEvidencesParams,
                ),
            ),
            model=DisputeEvidence,
        )

    def retrieve_evidence(
        self,
        evidence_token: str,
        *,
        dispute_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """
        Get a dispute's evidence metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        if not evidence_token:
            raise ValueError(f"Expected a non-empty value for `evidence_token` but received {evidence_token!r}")
        return self._get(
            f"/v1/disputes/{dispute_token}/evidences/{evidence_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeEvidence,
        )

    def upload_evidence(
        self,
        dispute_token: str,
        file: FileTypes,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Initiates the Dispute Evidence Upload, then uploads the file to the returned
        `upload_url`.
        """
        payload = self._client.disputes.initiate_evidence_upload(
            dispute_token, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body
        )
        if not payload.upload_url:
            raise ValueError("Missing 'upload_url' from response payload")
        files = {"file": file}
        options = make_request_options(extra_headers={"Authorization": Omit()})
        self._put(payload.upload_url, cast_to=NoneType, body=None, files=files, options=options)


class AsyncDisputes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDisputesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDisputesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisputesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncDisputesWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        reason: Literal[
            "ATM_CASH_MISDISPENSE",
            "CANCELLED",
            "DUPLICATED",
            "FRAUD_CARD_NOT_PRESENT",
            "FRAUD_CARD_PRESENT",
            "FRAUD_OTHER",
            "GOODS_SERVICES_NOT_AS_DESCRIBED",
            "GOODS_SERVICES_NOT_RECEIVED",
            "INCORRECT_AMOUNT",
            "MISSING_AUTH",
            "OTHER",
            "PROCESSING_ERROR",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
            "REFUND_NOT_PROCESSED",
        ],
        transaction_token: str,
        customer_filed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_note: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """
        Initiate a dispute.

        Args:
          amount: Amount to dispute

          reason: Reason for dispute

          transaction_token: Transaction to dispute

          customer_filed_date: Date the customer filed the dispute

          customer_note: Customer description of dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/disputes",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                    "transaction_token": transaction_token,
                    "customer_filed_date": customer_filed_date,
                    "customer_note": customer_note,
                },
                dispute_create_params.DisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    async def retrieve(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """
        Get dispute.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return await self._get(
            f"/v1/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    async def update(
        self,
        dispute_token: str,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        customer_filed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_note: str | NotGiven = NOT_GIVEN,
        reason: Literal[
            "ATM_CASH_MISDISPENSE",
            "CANCELLED",
            "DUPLICATED",
            "FRAUD_CARD_NOT_PRESENT",
            "FRAUD_CARD_PRESENT",
            "FRAUD_OTHER",
            "GOODS_SERVICES_NOT_AS_DESCRIBED",
            "GOODS_SERVICES_NOT_RECEIVED",
            "INCORRECT_AMOUNT",
            "MISSING_AUTH",
            "OTHER",
            "PROCESSING_ERROR",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
            "REFUND_NOT_PROCESSED",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """Update dispute.

        Can only be modified if status is `NEW`.

        Args:
          amount: Amount to dispute

          customer_filed_date: Date the customer filed the dispute

          customer_note: Customer description of dispute

          reason: Reason for dispute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return await self._patch(
            f"/v1/disputes/{dispute_token}",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "customer_filed_date": customer_filed_date,
                    "customer_note": customer_note,
                    "reason": reason,
                },
                dispute_update_params.DisputeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "ARBITRATION",
            "CASE_CLOSED",
            "CASE_WON",
            "NEW",
            "PENDING_CUSTOMER",
            "PREARBITRATION",
            "REPRESENTMENT",
            "SUBMITTED",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_tokens: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Dispute, AsyncCursorPage[Dispute]]:
        """List disputes.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: List disputes of a specific status.

          transaction_tokens: Transaction tokens to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/disputes",
            page=AsyncCursorPage[Dispute],
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
                        "transaction_tokens": transaction_tokens,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=Dispute,
        )

    async def delete(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """
        Withdraw dispute.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return await self._delete(
            f"/v1/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    async def delete_evidence(
        self,
        evidence_token: str,
        *,
        dispute_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """Soft delete evidence for a dispute.

        Evidence will not be reviewed or submitted
        by Lithic after it is withdrawn.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        if not evidence_token:
            raise ValueError(f"Expected a non-empty value for `evidence_token` but received {evidence_token!r}")
        return await self._delete(
            f"/v1/disputes/{dispute_token}/evidences/{evidence_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeEvidence,
        )

    async def initiate_evidence_upload(
        self,
        dispute_token: str,
        *,
        filename: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """Use this endpoint to upload evidences for the dispute.

        It will return a URL to
        upload your documents to. The URL will expire in 30 minutes.

        Uploaded documents must either be a `jpg`, `png` or `pdf` file, and each must be
        less than 5 GiB.

        Args:
          filename: Filename of the evidence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return await self._post(
            f"/v1/disputes/{dispute_token}/evidences",
            body=await async_maybe_transform(
                {"filename": filename}, dispute_initiate_evidence_upload_params.DisputeInitiateEvidenceUploadParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeEvidence,
        )

    def list_evidences(
        self,
        dispute_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DisputeEvidence, AsyncCursorPage[DisputeEvidence]]:
        """
        List evidence metadata for a dispute.

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
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return self._get_api_list(
            f"/v1/disputes/{dispute_token}/evidences",
            page=AsyncCursorPage[DisputeEvidence],
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
                    },
                    dispute_list_evidences_params.DisputeListEvidencesParams,
                ),
            ),
            model=DisputeEvidence,
        )

    async def retrieve_evidence(
        self,
        evidence_token: str,
        *,
        dispute_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """
        Get a dispute's evidence metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        if not evidence_token:
            raise ValueError(f"Expected a non-empty value for `evidence_token` but received {evidence_token!r}")
        return await self._get(
            f"/v1/disputes/{dispute_token}/evidences/{evidence_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeEvidence,
        )

    async def upload_evidence(
        self,
        dispute_token: str,
        file: FileTypes,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Initiates the Dispute Evidence Upload, then uploads the file to the returned
        `upload_url`.
        """
        payload = await self._client.disputes.initiate_evidence_upload(
            dispute_token, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body
        )
        if not payload.upload_url:
            raise ValueError("Missing 'upload_url' from response payload")
        files = {"file": file}
        options = make_request_options(extra_headers={"Authorization": Omit()})
        await self._put(payload.upload_url, cast_to=NoneType, body=None, files=files, options=options)


class DisputesWithRawResponse:
    def __init__(self, disputes: Disputes) -> None:
        self._disputes = disputes

        self.create = _legacy_response.to_raw_response_wrapper(
            disputes.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            disputes.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            disputes.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            disputes.delete,
        )
        self.delete_evidence = _legacy_response.to_raw_response_wrapper(
            disputes.delete_evidence,
        )
        self.initiate_evidence_upload = _legacy_response.to_raw_response_wrapper(
            disputes.initiate_evidence_upload,
        )
        self.list_evidences = _legacy_response.to_raw_response_wrapper(
            disputes.list_evidences,
        )
        self.retrieve_evidence = _legacy_response.to_raw_response_wrapper(
            disputes.retrieve_evidence,
        )


class AsyncDisputesWithRawResponse:
    def __init__(self, disputes: AsyncDisputes) -> None:
        self._disputes = disputes

        self.create = _legacy_response.async_to_raw_response_wrapper(
            disputes.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            disputes.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            disputes.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            disputes.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            disputes.delete,
        )
        self.delete_evidence = _legacy_response.async_to_raw_response_wrapper(
            disputes.delete_evidence,
        )
        self.initiate_evidence_upload = _legacy_response.async_to_raw_response_wrapper(
            disputes.initiate_evidence_upload,
        )
        self.list_evidences = _legacy_response.async_to_raw_response_wrapper(
            disputes.list_evidences,
        )
        self.retrieve_evidence = _legacy_response.async_to_raw_response_wrapper(
            disputes.retrieve_evidence,
        )


class DisputesWithStreamingResponse:
    def __init__(self, disputes: Disputes) -> None:
        self._disputes = disputes

        self.create = to_streamed_response_wrapper(
            disputes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = to_streamed_response_wrapper(
            disputes.list,
        )
        self.delete = to_streamed_response_wrapper(
            disputes.delete,
        )
        self.delete_evidence = to_streamed_response_wrapper(
            disputes.delete_evidence,
        )
        self.initiate_evidence_upload = to_streamed_response_wrapper(
            disputes.initiate_evidence_upload,
        )
        self.list_evidences = to_streamed_response_wrapper(
            disputes.list_evidences,
        )
        self.retrieve_evidence = to_streamed_response_wrapper(
            disputes.retrieve_evidence,
        )


class AsyncDisputesWithStreamingResponse:
    def __init__(self, disputes: AsyncDisputes) -> None:
        self._disputes = disputes

        self.create = async_to_streamed_response_wrapper(
            disputes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            disputes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            disputes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            disputes.delete,
        )
        self.delete_evidence = async_to_streamed_response_wrapper(
            disputes.delete_evidence,
        )
        self.initiate_evidence_upload = async_to_streamed_response_wrapper(
            disputes.initiate_evidence_upload,
        )
        self.list_evidences = async_to_streamed_response_wrapper(
            disputes.list_evidences,
        )
        self.retrieve_evidence = async_to_streamed_response_wrapper(
            disputes.retrieve_evidence,
        )
