# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, overload
from typing_extensions import Literal

from ..types import (
    AccountHolder,
    AccountHolderDocument,
    AccountHolderUpdateResponse,
    AccountHolderCreateWebhookResponse,
    AccountHolderListDocumentsResponse,
    shared_params,
    account_holder_create_params,
    account_holder_resubmit_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["AccountHolders", "AsyncAccountHolders"]


class AccountHolders(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        business_entity: account_holder_create_params.KYBBusinessEntity,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity],
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual],
        control_person: account_holder_create_params.KYBControlPerson,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        nature_of_business: str,
        tos_timestamp: str,
        website_url: str,
        workflow: Literal["KYB_BASIC", "KYB_BYO"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          business_entity: Information for business for which the account is being opened and KYB is being
              run.

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

          control_person: An individual with significant responsibility for managing the legal entity
              (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
              Officer, Managing Member, General Partner, President, Vice President, or
              Treasurer). This can be an executive, or someone who will have program-wide
              access to the cards that Lithic will provide. In some cases, this individual
              could also be a beneficial owner listed above. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section II) for more background.

          kyb_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          website_url: Company website URL.

          workflow: Specifies the type of KYB workflow to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        *,
        individual: account_holder_create_params.KYCIndividual,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str,
        workflow: Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          kyc_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYC workflow to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        *,
        workflow: Literal["KYC_EXEMPT"],
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"],
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          workflow: Specifies the workflow type. This must be 'KYC_EXEMPT'

          kyc_exemption_type: Specifies the type of KYC Exempt user

          first_name: The KYC Exempt user's first name

          last_name: The KYC Exempt user's last name

          email: The KYC Exempt user's email

          phone_number: The KYC Exempt user's phone number

          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @required_args(
        [
            "business_entity",
            "beneficial_owner_entities",
            "beneficial_owner_individuals",
            "control_person",
            "nature_of_business",
            "tos_timestamp",
            "website_url",
            "workflow",
        ],
        ["individual", "tos_timestamp", "workflow"],
        ["workflow", "kyc_exemption_type", "first_name", "last_name", "email", "phone_number"],
    )
    def create(
        self,
        *,
        business_entity: account_holder_create_params.KYBBusinessEntity | NotGiven = NOT_GIVEN,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity] | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        control_person: account_holder_create_params.KYBControlPerson | NotGiven = NOT_GIVEN,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str | str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        workflow: Literal["KYB_BASIC", "KYB_BYO"]
        | Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"]
        | Literal["KYC_EXEMPT"]
        | NotGiven = NOT_GIVEN,
        individual: account_holder_create_params.KYCIndividual | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"] | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          business_entity: Information for business for which the account is being opened and KYB is being
              run.

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

          control_person: An individual with significant responsibility for managing the legal entity
              (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
              Officer, Managing Member, General Partner, President, Vice President, or
              Treasurer). This can be an executive, or someone who will have program-wide
              access to the cards that Lithic will provide. In some cases, this individual
              could also be a beneficial owner listed above. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section II) for more background.

          kyb_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          website_url: Company website URL.

          workflow: Specifies the type of KYB workflow to run.

          individual: Information on individual for whom the account is being opened and KYC is being
              run.

          kyc_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          kyc_exemption_type: Specifies the type of KYC Exempt user

          first_name: The KYC Exempt user's first name

          last_name: The KYC Exempt user's last name

          email: The KYC Exempt user's email

          phone_number: The KYC Exempt user's phone number

          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/account_holders",
            body={
                "business_entity": business_entity,
                "beneficial_owner_entities": beneficial_owner_entities,
                "beneficial_owner_individuals": beneficial_owner_individuals,
                "control_person": control_person,
                "kyb_passed_timestamp": kyb_passed_timestamp,
                "nature_of_business": nature_of_business,
                "tos_timestamp": tos_timestamp,
                "website_url": website_url,
                "workflow": workflow,
                "individual": individual,
                "kyc_passed_timestamp": kyc_passed_timestamp,
                "kyc_exemption_type": kyc_exemption_type,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "address": address,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> AccountHolder:
        """Check the current status of a KYC or KYB evaluation."""
        return self._get(
            f"/account_holders/{account_holder_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolder,
        )

    def update(
        self,
        account_holder_token: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountHolderUpdateResponse:
        """
        Update the contact information associated with a particular account holder.

        Args:
          email: Account holder's email address. The primary purpose of this field is for
              cardholder identification and verification during the digital wallet
              tokenization process.

          phone_number: Account holder's phone number, entered in E.164 format. The primary purpose of
              this field is for cardholder identification and verification during the digital
              wallet tokenization process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/account_holders/{account_holder_token}",
            body={
                "email": email,
                "phone_number": phone_number,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderUpdateResponse,
        )

    def create_webhook(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountHolderCreateWebhookResponse:
        """
        Create a webhook to receive KYC or KYB evaluation events.

        There are two types of account holder webhooks:

        - `verification`: Webhook sent when the status of a KYC or KYB evaluation
          changes from `PENDING_DOCUMENT` (KYC) or `PENDING` (KYB) to `ACCEPTED` or
          `REJECTED`.
        - `document_upload_front`/`document_upload_back`: Webhook sent when a document
          upload fails.

        After a webhook has been created, this endpoint can be used to rotate a webhooks
        HMAC token or modify the registered URL. Only a single webhook is allowed per
        program. Since HMAC verification is available, the IP addresses from which
        KYC/KYB webhooks are sent are subject to change.

        Args:
          url: URL to receive webhook requests. Must be a valid HTTPS address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/webhooks/account_holders",
            body={"url": url},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderCreateWebhookResponse,
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
        return self._get(
            f"/account_holders/{account_holder_token}/documents",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderListDocumentsResponse,
        )

    def resubmit(
        self,
        account_holder_token: str,
        *,
        workflow: Literal["KYC_ADVANCED"],
        tos_timestamp: str,
        individual: account_holder_resubmit_params.Individual,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          individual: Information on individual for whom the account is being opened and KYC is being
              re-run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/account_holders/{account_holder_token}/resubmit",
            body={
                "workflow": workflow,
                "tos_timestamp": tos_timestamp,
                "individual": individual,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        return self._get(
            f"/account_holders/{account_holder_token}/documents/{document_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        """
        return self._post(
            f"/account_holders/{account_holder_token}/documents",
            body={"document_type": document_type},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderDocument,
        )


class AsyncAccountHolders(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        business_entity: account_holder_create_params.KYBBusinessEntity,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity],
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual],
        control_person: account_holder_create_params.KYBControlPerson,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        nature_of_business: str,
        tos_timestamp: str,
        website_url: str,
        workflow: Literal["KYB_BASIC", "KYB_BYO"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          business_entity: Information for business for which the account is being opened and KYB is being
              run.

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

          control_person: An individual with significant responsibility for managing the legal entity
              (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
              Officer, Managing Member, General Partner, President, Vice President, or
              Treasurer). This can be an executive, or someone who will have program-wide
              access to the cards that Lithic will provide. In some cases, this individual
              could also be a beneficial owner listed above. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section II) for more background.

          kyb_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          website_url: Company website URL.

          workflow: Specifies the type of KYB workflow to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        *,
        individual: account_holder_create_params.KYCIndividual,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str,
        workflow: Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          kyc_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYC workflow to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        *,
        workflow: Literal["KYC_EXEMPT"],
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"],
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          workflow: Specifies the workflow type. This must be 'KYC_EXEMPT'

          kyc_exemption_type: Specifies the type of KYC Exempt user

          first_name: The KYC Exempt user's first name

          last_name: The KYC Exempt user's last name

          email: The KYC Exempt user's email

          phone_number: The KYC Exempt user's phone number

          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @required_args(
        [
            "business_entity",
            "beneficial_owner_entities",
            "beneficial_owner_individuals",
            "control_person",
            "nature_of_business",
            "tos_timestamp",
            "website_url",
            "workflow",
        ],
        ["individual", "tos_timestamp", "workflow"],
        ["workflow", "kyc_exemption_type", "first_name", "last_name", "email", "phone_number"],
    )
    async def create(
        self,
        *,
        business_entity: account_holder_create_params.KYBBusinessEntity | NotGiven = NOT_GIVEN,
        beneficial_owner_entities: List[account_holder_create_params.KYBBeneficialOwnerEntity] | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: List[account_holder_create_params.KYBBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        control_person: account_holder_create_params.KYBControlPerson | NotGiven = NOT_GIVEN,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str | str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        workflow: Literal["KYB_BASIC", "KYB_BYO"]
        | Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"]
        | Literal["KYC_EXEMPT"]
        | NotGiven = NOT_GIVEN,
        individual: account_holder_create_params.KYCIndividual | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"] | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        address: shared_params.Address | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          business_entity: Information for business for which the account is being opened and KYB is being
              run.

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

          control_person: An individual with significant responsibility for managing the legal entity
              (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
              Officer, Managing Member, General Partner, President, Vice President, or
              Treasurer). This can be an executive, or someone who will have program-wide
              access to the cards that Lithic will provide. In some cases, this individual
              could also be a beneficial owner listed above. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section II) for more background.

          kyb_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          website_url: Company website URL.

          workflow: Specifies the type of KYB workflow to run.

          individual: Information on individual for whom the account is being opened and KYC is being
              run.

          kyc_passed_timestamp: An ISO 8601 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          kyc_exemption_type: Specifies the type of KYC Exempt user

          first_name: The KYC Exempt user's first name

          last_name: The KYC Exempt user's last name

          email: The KYC Exempt user's email

          phone_number: The KYC Exempt user's phone number

          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/account_holders",
            body={
                "business_entity": business_entity,
                "beneficial_owner_entities": beneficial_owner_entities,
                "beneficial_owner_individuals": beneficial_owner_individuals,
                "control_person": control_person,
                "kyb_passed_timestamp": kyb_passed_timestamp,
                "nature_of_business": nature_of_business,
                "tos_timestamp": tos_timestamp,
                "website_url": website_url,
                "workflow": workflow,
                "individual": individual,
                "kyc_passed_timestamp": kyc_passed_timestamp,
                "kyc_exemption_type": kyc_exemption_type,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "address": address,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
    ) -> AccountHolder:
        """Check the current status of a KYC or KYB evaluation."""
        return await self._get(
            f"/account_holders/{account_holder_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolder,
        )

    async def update(
        self,
        account_holder_token: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountHolderUpdateResponse:
        """
        Update the contact information associated with a particular account holder.

        Args:
          email: Account holder's email address. The primary purpose of this field is for
              cardholder identification and verification during the digital wallet
              tokenization process.

          phone_number: Account holder's phone number, entered in E.164 format. The primary purpose of
              this field is for cardholder identification and verification during the digital
              wallet tokenization process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/account_holders/{account_holder_token}",
            body={
                "email": email,
                "phone_number": phone_number,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderUpdateResponse,
        )

    async def create_webhook(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AccountHolderCreateWebhookResponse:
        """
        Create a webhook to receive KYC or KYB evaluation events.

        There are two types of account holder webhooks:

        - `verification`: Webhook sent when the status of a KYC or KYB evaluation
          changes from `PENDING_DOCUMENT` (KYC) or `PENDING` (KYB) to `ACCEPTED` or
          `REJECTED`.
        - `document_upload_front`/`document_upload_back`: Webhook sent when a document
          upload fails.

        After a webhook has been created, this endpoint can be used to rotate a webhooks
        HMAC token or modify the registered URL. Only a single webhook is allowed per
        program. Since HMAC verification is available, the IP addresses from which
        KYC/KYB webhooks are sent are subject to change.

        Args:
          url: URL to receive webhook requests. Must be a valid HTTPS address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/webhooks/account_holders",
            body={"url": url},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderCreateWebhookResponse,
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
        return await self._get(
            f"/account_holders/{account_holder_token}/documents",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderListDocumentsResponse,
        )

    async def resubmit(
        self,
        account_holder_token: str,
        *,
        workflow: Literal["KYC_ADVANCED"],
        tos_timestamp: str,
        individual: account_holder_resubmit_params.Individual,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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
          tos_timestamp: An ISO 8601 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          individual: Information on individual for whom the account is being opened and KYC is being
              re-run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/account_holders/{account_holder_token}/resubmit",
            body={
                "workflow": workflow,
                "tos_timestamp": tos_timestamp,
                "individual": individual,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        return await self._get(
            f"/account_holders/{account_holder_token}/documents/{document_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        """
        return await self._post(
            f"/account_holders/{account_holder_token}/documents",
            body={"document_type": document_type},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AccountHolderDocument,
        )
