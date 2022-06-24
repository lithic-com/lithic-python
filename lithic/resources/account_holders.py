# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options
from ..types.account_holder import *
from ..types.account_holder_document import *
from ..types.account_holder_create_params import AccountHolderCreateParams
from ..types.account_holder_resubmit_params import AccountHolderResubmitParams
from ..types.account_holder_create_webhook_params import (
    AccountHolderCreateWebhookParams,
)
from ..types.account_holder_upload_document_params import (
    AccountHolderUploadDocumentParams,
)
from ..types.account_holder_create_webhook_response import *
from ..types.account_holder_list_documents_response import *

__all__ = ["AccountHolders", "AsyncAccountHolders"]


class AccountHolders(SyncAPIResource):
    def create(
        self,
        body: AccountHolderCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/account_holders",
            body=body,
            options=options,
            cast_to=AccountHolder,
        )

    def retrieve(
        self,
        account_holder_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolder:
        """Check the current status of a KYC or KYB evaluation."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/account_holders/{account_holder_token}",
            options=options,
            cast_to=AccountHolder,
        )

    def create_webhook(
        self,
        body: AccountHolderCreateWebhookParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderCreateWebhookResponse:
        """Create a webhook to receive KYC or KYB evaluation events.

        There are two types of account holder webhooks:

        - `verification`: Webhook sent when the status of a KYC or KYB evaluation
          changes from `PENDING_DOCUMENT` (KYC) or `PENDING` (KYB) to `ACCEPTED` or
          `REJECTED`.
        - `document_upload_front`/`document_upload_back`: Webhook sent when a document
          upload fails.

        After a webhook has been created, this endpoint can be used to rotate a webhooks
        HMAC token or modify the registered URL. Only a single webhook is allowed per
        program.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/webhooks/account_holders",
            body=body,
            options=options,
            cast_to=AccountHolderCreateWebhookResponse,
        )

    def list_documents(
        self,
        account_holder_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderListDocumentsResponse:
        """
        Retrieve the status of account holder document uploads, or retrieve the upload
        URLs to process your image uploads.

        Note that this is not equivalent to checking the status of the KYC evaluation
        overall (a document may be successfully uploaded but not be sufficient for KYC
        to pass).

        In the event your upload URLs have expired, calling this endpoint will refresh
        them. Similarly, in the event a previous account holder document upload has
        failed, you can use this endpoint to get a new upload URL for the failed image
        upload.

        When a new document upload is generated for a failed attempt, the response will
        show an additional entry in the `required_document_uploads` list in a `PENDING`
        state for the corresponding `image_type`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/account_holders/{account_holder_token}/documents",
            options=options,
            cast_to=AccountHolderListDocumentsResponse,
        )

    def resubmit(
        self,
        account_holder_token: str,
        body: AccountHolderResubmitParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolder:
        """Resubmit a KYC submission.

        This endpoint should be used in cases where a KYC submission returned a
        `PENDING_RESUBMIT` result, meaning one or more critical KYC fields may have been
        mis-entered and the individual's identity has not yet been successfully
        verified. This step must be completed in order to proceed with the KYC
        evaluation.

        Two resubmission attempts are permitted via this endpoint before a `REJECTED`
        status is returned and the account creation process is ended.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/account_holders/{account_holder_token}/resubmit",
            body=body,
            options=options,
            cast_to=AccountHolder,
        )

    def retrieve_document(
        self,
        account_holder_token: str,
        document_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderDocument:
        """
        Check the status of an account holder document upload, or retrieve the upload
        URLs to process your image uploads.

        Note that this is not equivalent to checking the status of the KYC evaluation
        overall (a document may be successfully uploaded but not be sufficient for KYC
        to pass).

        In the event your upload URLs have expired, calling this endpoint will refresh
        them. Similarly, in the event a document upload has failed, you can use this
        endpoint to get a new upload URL for the failed image upload.

        When a new account holder document upload is generated for a failed attempt, the
        response will show an additional entry in the `required_document_uploads` array
        in a `PENDING` state for the corresponding `image_type`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/account_holders/{account_holder_token}/documents/{document_token}",
            options=options,
            cast_to=AccountHolderDocument,
        )

    def upload_document(
        self,
        account_holder_token: str,
        body: AccountHolderUploadDocumentParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderDocument:
        """
        Use this endpoint to identify which type of supported government-issued
        documentation you will upload for further verification. It will return two URLs
        to upload your document images to - one for the front image and one for the back
        image.

        This endpoint is only valid for evaluations in a `PENDING_DOCUMENT` state.

        Uploaded images must either be a `jpg` or `png` file, and each must be less than
        15 MiB. Once both required uploads have been successfully completed, your
        document will be run through KYC verification.

        If you have registered a webhook, you will receive evaluation updates for any
        document submission evaluations, as well as for any failed document uploads.

        Two document submission attempts are permitted via this endpoint before a
        `REJECTED` status is returned and the account creation process is ended.
        Currently only one type of account holder document is supported per KYC
        verification.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/account_holders/{account_holder_token}/documents",
            body=body,
            options=options,
            cast_to=AccountHolderDocument,
        )


class AsyncAccountHolders(AsyncAPIResource):
    async def create(
        self,
        body: AccountHolderCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/account_holders",
            body=body,
            options=options,
            cast_to=AccountHolder,
        )

    async def retrieve(
        self,
        account_holder_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolder:
        """Check the current status of a KYC or KYB evaluation."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/account_holders/{account_holder_token}",
            options=options,
            cast_to=AccountHolder,
        )

    async def create_webhook(
        self,
        body: AccountHolderCreateWebhookParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderCreateWebhookResponse:
        """Create a webhook to receive KYC or KYB evaluation events.

        There are two types of account holder webhooks:

        - `verification`: Webhook sent when the status of a KYC or KYB evaluation
          changes from `PENDING_DOCUMENT` (KYC) or `PENDING` (KYB) to `ACCEPTED` or
          `REJECTED`.
        - `document_upload_front`/`document_upload_back`: Webhook sent when a document
          upload fails.

        After a webhook has been created, this endpoint can be used to rotate a webhooks
        HMAC token or modify the registered URL. Only a single webhook is allowed per
        program.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/webhooks/account_holders",
            body=body,
            options=options,
            cast_to=AccountHolderCreateWebhookResponse,
        )

    async def list_documents(
        self,
        account_holder_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderListDocumentsResponse:
        """
        Retrieve the status of account holder document uploads, or retrieve the upload
        URLs to process your image uploads.

        Note that this is not equivalent to checking the status of the KYC evaluation
        overall (a document may be successfully uploaded but not be sufficient for KYC
        to pass).

        In the event your upload URLs have expired, calling this endpoint will refresh
        them. Similarly, in the event a previous account holder document upload has
        failed, you can use this endpoint to get a new upload URL for the failed image
        upload.

        When a new document upload is generated for a failed attempt, the response will
        show an additional entry in the `required_document_uploads` list in a `PENDING`
        state for the corresponding `image_type`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/account_holders/{account_holder_token}/documents",
            options=options,
            cast_to=AccountHolderListDocumentsResponse,
        )

    async def resubmit(
        self,
        account_holder_token: str,
        body: AccountHolderResubmitParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolder:
        """Resubmit a KYC submission.

        This endpoint should be used in cases where a KYC submission returned a
        `PENDING_RESUBMIT` result, meaning one or more critical KYC fields may have been
        mis-entered and the individual's identity has not yet been successfully
        verified. This step must be completed in order to proceed with the KYC
        evaluation.

        Two resubmission attempts are permitted via this endpoint before a `REJECTED`
        status is returned and the account creation process is ended.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/account_holders/{account_holder_token}/resubmit",
            body=body,
            options=options,
            cast_to=AccountHolder,
        )

    async def retrieve_document(
        self,
        account_holder_token: str,
        document_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderDocument:
        """
        Check the status of an account holder document upload, or retrieve the upload
        URLs to process your image uploads.

        Note that this is not equivalent to checking the status of the KYC evaluation
        overall (a document may be successfully uploaded but not be sufficient for KYC
        to pass).

        In the event your upload URLs have expired, calling this endpoint will refresh
        them. Similarly, in the event a document upload has failed, you can use this
        endpoint to get a new upload URL for the failed image upload.

        When a new account holder document upload is generated for a failed attempt, the
        response will show an additional entry in the `required_document_uploads` array
        in a `PENDING` state for the corresponding `image_type`.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/account_holders/{account_holder_token}/documents/{document_token}",
            options=options,
            cast_to=AccountHolderDocument,
        )

    async def upload_document(
        self,
        account_holder_token: str,
        body: AccountHolderUploadDocumentParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AccountHolderDocument:
        """
        Use this endpoint to identify which type of supported government-issued
        documentation you will upload for further verification. It will return two URLs
        to upload your document images to - one for the front image and one for the back
        image.

        This endpoint is only valid for evaluations in a `PENDING_DOCUMENT` state.

        Uploaded images must either be a `jpg` or `png` file, and each must be less than
        15 MiB. Once both required uploads have been successfully completed, your
        document will be run through KYC verification.

        If you have registered a webhook, you will receive evaluation updates for any
        document submission evaluations, as well as for any failed document uploads.

        Two document submission attempts are permitted via this endpoint before a
        `REJECTED` status is returned and the account creation process is ended.
        Currently only one type of account holder document is supported per KYC
        verification.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/account_holders/{account_holder_token}/documents",
            body=body,
            options=options,
            cast_to=AccountHolderDocument,
        )
