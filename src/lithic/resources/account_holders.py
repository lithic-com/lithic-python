# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, overload
from typing_extensions import Literal

import httpx

from ..types import (
    AccountHolder,
    AccountHolderDocument,
    AccountHolderUpdateResponse,
    AccountHolderListDocumentsResponse,
    shared_params,
    account_holder_create_params,
    account_holder_update_params,
    account_holder_resubmit_params,
    account_holder_upload_document_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Lithic, AsyncLithic

__all__ = ["AccountHolders", "AsyncAccountHolders"]


class AccountHolders(SyncAPIResource):
    with_raw_response: AccountHoldersWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = AccountHoldersWithRawResponse(self)

    @overload
    def create(
        self,
        *,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity],
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual],
        business_entity: account_holder_create_params.KYBBusinessEntity,
        control_person: account_holder_create_params.KYBControlPerson,
        nature_of_business: str,
        tos_timestamp: str,
        workflow: Literal["KYB_BASIC", "KYB_BYO"],
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.

        Args:
          beneficial_owner_entities: List of all entities with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an entity,
              please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section I) for more background. If no business owner is an entity, pass in an
              empty list. However, either this parameter or `beneficial_owner_individuals`
              must be populated. on entities that should be included.

          beneficial_owner_individuals: List of all individuals with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an
              individual, please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section I) for more background on individuals that should be included. If no
              individual is an entity, pass in an empty list. However, either this parameter
              or `beneficial_owner_entities` must be populated.

          business_entity: Information for business for which the account is being opened and KYB is being
              run.

          control_person: An individual with significant responsibility for managing the legal entity
              (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
              Officer, Managing Member, General Partner, President, Vice President, or
              Treasurer). This can be an executive, or someone who will have program-wide
              access to the cards that Lithic will provide. In some cases, this individual
              could also be a beneficial owner listed above. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section II) for more background.

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYB workflow to run.

          kyb_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          website_url: Company website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        individual: account_holder_create_params.KYCIndividual,
        tos_timestamp: str,
        workflow: Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"],
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.

        Args:
          individual: Information on individual for whom the account is being opened and KYC is being
              run.

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYC workflow to run.

          kyc_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        email: str,
        first_name: str,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"],
        last_name: str,
        phone_number: str,
        workflow: Literal["KYC_EXEMPT"],
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.

        Args:
          email: The KYC Exempt user's email

          first_name: The KYC Exempt user's first name

          kyc_exemption_type: Specifies the type of KYC Exempt user

          last_name: The KYC Exempt user's last name

          phone_number: The KYC Exempt user's phone number

          workflow: Specifies the workflow type. This must be 'KYC_EXEMPT'

          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          business_account_token: Only applicable for customers using the KYC-Exempt workflow to enroll authorized
              users of businesses. Pass the account_token of the enrolled business associated
              with the AUTHORIZED_USER in this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        [
            "beneficial_owner_entities",
            "beneficial_owner_individuals",
            "business_entity",
            "control_person",
            "nature_of_business",
            "tos_timestamp",
            "workflow",
        ],
        ["individual", "tos_timestamp", "workflow"],
        ["email", "first_name", "kyc_exemption_type", "last_name", "phone_number", "workflow"],
    )
    def create(
        self,
        *,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity] | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_create_params.KYBBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_create_params.KYBControlPerson | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str | NotGiven = NOT_GIVEN,
        workflow: Literal["KYB_BASIC", "KYB_BYO"]
        | Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"]
        | Literal["KYC_EXEMPT"],
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        individual: account_holder_create_params.KYCIndividual | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        return self._post(
            "/account_holders",
            body=maybe_transform(
                {
                    "beneficial_owner_entities": beneficial_owner_entities,
                    "beneficial_owner_individuals": beneficial_owner_individuals,
                    "business_entity": business_entity,
                    "control_person": control_person,
                    "nature_of_business": nature_of_business,
                    "tos_timestamp": tos_timestamp,
                    "workflow": workflow,
                    "kyb_passed_timestamp": kyb_passed_timestamp,
                    "website_url": website_url,
                    "individual": individual,
                    "kyc_passed_timestamp": kyc_passed_timestamp,
                    "email": email,
                    "first_name": first_name,
                    "kyc_exemption_type": kyc_exemption_type,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "address": address,
                    "business_account_token": business_account_token,
                },
                account_holder_create_params.AccountHolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolder,
        )

    def retrieve(
        self,
        account_holder_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolder:
        """
        Get an Individual or Business Account Holder and/or their KYC or KYB evaluation
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/account_holders/{account_holder_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolder,
        )

    def update(
        self,
        account_holder_token: str,
        *,
        business_account_token: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder.

        Args:
          business_account_token: Only applicable for customers using the KYC-Exempt workflow to enroll authorized
              users of businesses. Pass the account_token of the enrolled business associated
              with the AUTHORIZED_USER in this field.

          email: Account holder's email address. The primary purpose of this field is for
              cardholder identification and verification during the digital wallet
              tokenization process.

          phone_number: Account holder's phone number, entered in E.164 format. The primary purpose of
              this field is for cardholder identification and verification during the digital
              wallet tokenization process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/account_holders/{account_holder_token}",
            body=maybe_transform(
                {
                    "business_account_token": business_account_token,
                    "email": email,
                    "phone_number": phone_number,
                },
                account_holder_update_params.AccountHolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolderUpdateResponse,
        )

    def list_documents(
        self,
        account_holder_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/account_holders/{account_holder_token}/documents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderListDocumentsResponse,
        )

    def resubmit(
        self,
        account_holder_token: str,
        *,
        individual: account_holder_resubmit_params.Individual,
        tos_timestamp: str,
        workflow: Literal["KYC_ADVANCED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """Resubmit a KYC submission.

        This endpoint should be used in cases where a KYC
        submission returned a `PENDING_RESUBMIT` result, meaning one or more critical
        KYC fields may have been mis-entered and the individual's identity has not yet
        been successfully verified. This step must be completed in order to proceed with
        the KYC evaluation.

        Two resubmission attempts are permitted via this endpoint before a `REJECTED`
        status is returned and the account creation process is ended.

        Args:
          individual: Information on individual for whom the account is being opened and KYC is being
              re-run.

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/account_holders/{account_holder_token}/resubmit",
            body=maybe_transform(
                {
                    "individual": individual,
                    "tos_timestamp": tos_timestamp,
                    "workflow": workflow,
                },
                account_holder_resubmit_params.AccountHolderResubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolder,
        )

    def retrieve_document(
        self,
        document_token: str,
        *,
        account_holder_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/account_holders/{account_holder_token}/documents/{document_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderDocument,
        )

    def upload_document(
        self,
        account_holder_token: str,
        *,
        document_type: Literal["commercial_license", "drivers_license", "passport", "passport_card", "visa"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

        Args:
          document_type: Type of the document to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/account_holders/{account_holder_token}/documents",
            body=maybe_transform(
                {"document_type": document_type},
                account_holder_upload_document_params.AccountHolderUploadDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolderDocument,
        )


class AsyncAccountHolders(AsyncAPIResource):
    with_raw_response: AsyncAccountHoldersWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAccountHoldersWithRawResponse(self)

    @overload
    async def create(
        self,
        *,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity],
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual],
        business_entity: account_holder_create_params.KYBBusinessEntity,
        control_person: account_holder_create_params.KYBControlPerson,
        nature_of_business: str,
        tos_timestamp: str,
        workflow: Literal["KYB_BASIC", "KYB_BYO"],
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.

        Args:
          beneficial_owner_entities: List of all entities with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an entity,
              please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section I) for more background. If no business owner is an entity, pass in an
              empty list. However, either this parameter or `beneficial_owner_individuals`
              must be populated. on entities that should be included.

          beneficial_owner_individuals: List of all individuals with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an
              individual, please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section I) for more background on individuals that should be included. If no
              individual is an entity, pass in an empty list. However, either this parameter
              or `beneficial_owner_entities` must be populated.

          business_entity: Information for business for which the account is being opened and KYB is being
              run.

          control_person: An individual with significant responsibility for managing the legal entity
              (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
              Officer, Managing Member, General Partner, President, Vice President, or
              Treasurer). This can be an executive, or someone who will have program-wide
              access to the cards that Lithic will provide. In some cases, this individual
              could also be a beneficial owner listed above. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section II) for more background.

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYB workflow to run.

          kyb_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          website_url: Company website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        individual: account_holder_create_params.KYCIndividual,
        tos_timestamp: str,
        workflow: Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"],
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.

        Args:
          individual: Information on individual for whom the account is being opened and KYC is being
              run.

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYC workflow to run.

          kyc_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        email: str,
        first_name: str,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"],
        last_name: str,
        phone_number: str,
        workflow: Literal["KYC_EXEMPT"],
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """
        Run an individual or business's information through the Customer Identification
        Program (CIP) and return an `account_token` if the status is accepted or pending
        (i.e., further action required). All calls to this endpoint will return an
        immediate response - though in some cases, the response may indicate the
        workflow is under review or further action will be needed to complete the
        account creation process. This endpoint can only be used on accounts that are
        part of the program the calling API key manages.

        Args:
          email: The KYC Exempt user's email

          first_name: The KYC Exempt user's first name

          kyc_exemption_type: Specifies the type of KYC Exempt user

          last_name: The KYC Exempt user's last name

          phone_number: The KYC Exempt user's phone number

          workflow: Specifies the workflow type. This must be 'KYC_EXEMPT'

          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          business_account_token: Only applicable for customers using the KYC-Exempt workflow to enroll authorized
              users of businesses. Pass the account_token of the enrolled business associated
              with the AUTHORIZED_USER in this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        [
            "beneficial_owner_entities",
            "beneficial_owner_individuals",
            "business_entity",
            "control_person",
            "nature_of_business",
            "tos_timestamp",
            "workflow",
        ],
        ["individual", "tos_timestamp", "workflow"],
        ["email", "first_name", "kyc_exemption_type", "last_name", "phone_number", "workflow"],
    )
    async def create(
        self,
        *,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity] | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_create_params.KYBBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_create_params.KYBControlPerson | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str | NotGiven = NOT_GIVEN,
        workflow: Literal["KYB_BASIC", "KYB_BYO"]
        | Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"]
        | Literal["KYC_EXEMPT"],
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        individual: account_holder_create_params.KYCIndividual | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = 300,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        return await self._post(
            "/account_holders",
            body=maybe_transform(
                {
                    "beneficial_owner_entities": beneficial_owner_entities,
                    "beneficial_owner_individuals": beneficial_owner_individuals,
                    "business_entity": business_entity,
                    "control_person": control_person,
                    "nature_of_business": nature_of_business,
                    "tos_timestamp": tos_timestamp,
                    "workflow": workflow,
                    "kyb_passed_timestamp": kyb_passed_timestamp,
                    "website_url": website_url,
                    "individual": individual,
                    "kyc_passed_timestamp": kyc_passed_timestamp,
                    "email": email,
                    "first_name": first_name,
                    "kyc_exemption_type": kyc_exemption_type,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "address": address,
                    "business_account_token": business_account_token,
                },
                account_holder_create_params.AccountHolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolder,
        )

    async def retrieve(
        self,
        account_holder_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolder:
        """
        Get an Individual or Business Account Holder and/or their KYC or KYB evaluation
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/account_holders/{account_holder_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolder,
        )

    async def update(
        self,
        account_holder_token: str,
        *,
        business_account_token: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder.

        Args:
          business_account_token: Only applicable for customers using the KYC-Exempt workflow to enroll authorized
              users of businesses. Pass the account_token of the enrolled business associated
              with the AUTHORIZED_USER in this field.

          email: Account holder's email address. The primary purpose of this field is for
              cardholder identification and verification during the digital wallet
              tokenization process.

          phone_number: Account holder's phone number, entered in E.164 format. The primary purpose of
              this field is for cardholder identification and verification during the digital
              wallet tokenization process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/account_holders/{account_holder_token}",
            body=maybe_transform(
                {
                    "business_account_token": business_account_token,
                    "email": email,
                    "phone_number": phone_number,
                },
                account_holder_update_params.AccountHolderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolderUpdateResponse,
        )

    async def list_documents(
        self,
        account_holder_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/account_holders/{account_holder_token}/documents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderListDocumentsResponse,
        )

    async def resubmit(
        self,
        account_holder_token: str,
        *,
        individual: account_holder_resubmit_params.Individual,
        tos_timestamp: str,
        workflow: Literal["KYC_ADVANCED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AccountHolder:
        """Resubmit a KYC submission.

        This endpoint should be used in cases where a KYC
        submission returned a `PENDING_RESUBMIT` result, meaning one or more critical
        KYC fields may have been mis-entered and the individual's identity has not yet
        been successfully verified. This step must be completed in order to proceed with
        the KYC evaluation.

        Two resubmission attempts are permitted via this endpoint before a `REJECTED`
        status is returned and the account creation process is ended.

        Args:
          individual: Information on individual for whom the account is being opened and KYC is being
              re-run.

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/account_holders/{account_holder_token}/resubmit",
            body=maybe_transform(
                {
                    "individual": individual,
                    "tos_timestamp": tos_timestamp,
                    "workflow": workflow,
                },
                account_holder_resubmit_params.AccountHolderResubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolder,
        )

    async def retrieve_document(
        self,
        document_token: str,
        *,
        account_holder_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/account_holders/{account_holder_token}/documents/{document_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderDocument,
        )

    async def upload_document(
        self,
        account_holder_token: str,
        *,
        document_type: Literal["commercial_license", "drivers_license", "passport", "passport_card", "visa"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

        Args:
          document_type: Type of the document to upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/account_holders/{account_holder_token}/documents",
            body=maybe_transform(
                {"document_type": document_type},
                account_holder_upload_document_params.AccountHolderUploadDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AccountHolderDocument,
        )


class AccountHoldersWithRawResponse:
    def __init__(self, account_holders: AccountHolders) -> None:
        self.create = to_raw_response_wrapper(
            account_holders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            account_holders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            account_holders.update,
        )
        self.list_documents = to_raw_response_wrapper(
            account_holders.list_documents,
        )
        self.resubmit = to_raw_response_wrapper(
            account_holders.resubmit,
        )
        self.retrieve_document = to_raw_response_wrapper(
            account_holders.retrieve_document,
        )
        self.upload_document = to_raw_response_wrapper(
            account_holders.upload_document,
        )


class AsyncAccountHoldersWithRawResponse:
    def __init__(self, account_holders: AsyncAccountHolders) -> None:
        self.create = async_to_raw_response_wrapper(
            account_holders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            account_holders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            account_holders.update,
        )
        self.list_documents = async_to_raw_response_wrapper(
            account_holders.list_documents,
        )
        self.resubmit = async_to_raw_response_wrapper(
            account_holders.resubmit,
        )
        self.retrieve_document = async_to_raw_response_wrapper(
            account_holders.retrieve_document,
        )
        self.upload_document = async_to_raw_response_wrapper(
            account_holders.upload_document,
        )
