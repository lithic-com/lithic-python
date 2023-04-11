# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

from ..types import (
    Dispute,
    DisputeEvidence,
    DisputeInitiateEvidenceUploadResponse,
    dispute_list_params,
    dispute_create_params,
    dispute_update_params,
    dispute_list_evidences_params,
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
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Disputes", "AsyncDisputes"]


class Disputes(SyncAPIResource):
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
            "REFUND_NOT_PROCESSED",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
        ],
        transaction_token: str,
        customer_filed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_note: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/disputes",
            body=maybe_transform(
                {
                    "amount": amount,
                    "customer_filed_date": customer_filed_date,
                    "reason": reason,
                    "transaction_token": transaction_token,
                    "customer_note": customer_note,
                },
                dispute_create_params.DisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """Get dispute."""
        return self._get(
            f"/disputes/{dispute_token}",
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
            "REFUND_NOT_PROCESSED",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/disputes/{dispute_token}",
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
            "NEW",
            "PENDING_CUSTOMER",
            "SUBMITTED",
            "REPRESENTMENT",
            "PREARBITRATION",
            "ARBITRATION",
            "CASE_WON",
            "CASE_CLOSED",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Dispute]:
        """List disputes.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          status: List disputes of a specific status.

          transaction_token: List disputes of a given transaction token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/disputes",
            page=SyncCursorPage[Dispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "transaction_token": transaction_token,
                        "status": status,
                        "page_size": page_size,
                        "begin": begin,
                        "end": end,
                        "starting_after": starting_after,
                        "ending_before": ending_before,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Dispute:
        """Withdraw dispute."""
        return self._delete(
            f"/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DisputeEvidence:
        """Soft delete evidence for a dispute.

        Evidence will not be reviewed or submitted
        by Lithic after it is withdrawn.
        """
        return self._delete(
            f"/disputes/{dispute_token}/evidences/{evidence_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DisputeEvidence,
        )

    def initiate_evidence_upload(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DisputeInitiateEvidenceUploadResponse:
        """Use this endpoint to upload evidences for the dispute.

        It will return a URL to
        upload your documents to. The URL will expire in 30 minutes.

        Uploaded documents must either be a `jpg`, `png` or `pdf` file, and each must be
        less than 5 GiB.
        """
        return self._post(
            f"/disputes/{dispute_token}/evidences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DisputeInitiateEvidenceUploadResponse,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[DisputeEvidence]:
        """
        List evidence metadata for a dispute.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/disputes/{dispute_token}/evidences",
            page=SyncCursorPage[DisputeEvidence],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "begin": begin,
                        "end": end,
                        "starting_after": starting_after,
                        "ending_before": ending_before,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """Get a dispute's evidence metadata."""
        return self._get(
            f"/disputes/{dispute_token}/evidences/{evidence_token}",
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
            "REFUND_NOT_PROCESSED",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
        ],
        transaction_token: str,
        customer_filed_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_note: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/disputes",
            body=maybe_transform(
                {
                    "amount": amount,
                    "customer_filed_date": customer_filed_date,
                    "reason": reason,
                    "transaction_token": transaction_token,
                    "customer_note": customer_note,
                },
                dispute_create_params.DisputeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Dispute:
        """Get dispute."""
        return await self._get(
            f"/disputes/{dispute_token}",
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
            "REFUND_NOT_PROCESSED",
            "RECURRING_TRANSACTION_NOT_CANCELLED",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/disputes/{dispute_token}",
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
            "NEW",
            "PENDING_CUSTOMER",
            "SUBMITTED",
            "REPRESENTMENT",
            "PREARBITRATION",
            "ARBITRATION",
            "CASE_WON",
            "CASE_CLOSED",
        ]
        | NotGiven = NOT_GIVEN,
        transaction_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Dispute, AsyncCursorPage[Dispute]]:
        """List disputes.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          status: List disputes of a specific status.

          transaction_token: List disputes of a given transaction token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/disputes",
            page=AsyncCursorPage[Dispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "transaction_token": transaction_token,
                        "status": status,
                        "page_size": page_size,
                        "begin": begin,
                        "end": end,
                        "starting_after": starting_after,
                        "ending_before": ending_before,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Dispute:
        """Withdraw dispute."""
        return await self._delete(
            f"/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DisputeEvidence:
        """Soft delete evidence for a dispute.

        Evidence will not be reviewed or submitted
        by Lithic after it is withdrawn.
        """
        return await self._delete(
            f"/disputes/{dispute_token}/evidences/{evidence_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DisputeEvidence,
        )

    async def initiate_evidence_upload(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> DisputeInitiateEvidenceUploadResponse:
        """Use this endpoint to upload evidences for the dispute.

        It will return a URL to
        upload your documents to. The URL will expire in 30 minutes.

        Uploaded documents must either be a `jpg`, `png` or `pdf` file, and each must be
        less than 5 GiB.
        """
        return await self._post(
            f"/disputes/{dispute_token}/evidences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DisputeInitiateEvidenceUploadResponse,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DisputeEvidence, AsyncCursorPage[DisputeEvidence]]:
        """
        List evidence metadata for a dispute.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/disputes/{dispute_token}/evidences",
            page=AsyncCursorPage[DisputeEvidence],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "begin": begin,
                        "end": end,
                        "starting_after": starting_after,
                        "ending_before": ending_before,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> DisputeEvidence:
        """Get a dispute's evidence metadata."""
        return await self._get(
            f"/disputes/{dispute_token}/evidences/{evidence_token}",
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
