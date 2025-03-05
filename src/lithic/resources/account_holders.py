# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, cast
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from .. import _legacy_response
from ..types import (
    account_holder_list_params,
    account_holder_create_params,
    account_holder_update_params,
    account_holder_upload_document_params,
    account_holder_simulate_enrollment_review_params,
    account_holder_simulate_enrollment_document_review_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._constants import DEFAULT_TIMEOUT
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account_holder import AccountHolder
from ..types.shared.document import Document
from ..types.address_update_param import AddressUpdateParam
from ..types.shared_params.address import Address
from ..types.account_holder_create_response import AccountHolderCreateResponse
from ..types.account_holder_update_response import AccountHolderUpdateResponse
from ..types.account_holder_list_documents_response import AccountHolderListDocumentsResponse
from ..types.account_holder_simulate_enrollment_review_response import AccountHolderSimulateEnrollmentReviewResponse

__all__ = ["AccountHolders", "AsyncAccountHolders"]


class AccountHolders(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountHoldersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AccountHoldersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountHoldersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AccountHoldersWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        beneficial_owner_entities: Iterable[account_holder_create_params.KYBBeneficialOwnerEntity],
        beneficial_owner_individuals: Iterable[account_holder_create_params.KYBBeneficialOwnerIndividual],
        business_entity: account_holder_create_params.KYBBusinessEntity,
        control_person: account_holder_create_params.KYBControlPerson,
        nature_of_business: str,
        tos_timestamp: str,
        workflow: Literal["KYB_BASIC", "KYB_BYO"],
        external_id: str | NotGiven = NOT_GIVEN,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Create an account holder and initiate the appropriate onboarding workflow.
        Account holders and accounts have a 1:1 relationship. When an account holder is
        successfully created an associated account is also created. All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the enrollment is under review or further action will be needed to
        complete the account enrollment process. This endpoint can only be used on
        accounts that are part of the program that the calling API key manages.

        Args:
          beneficial_owner_entities: List of all entities with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an entity,
              please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section I) for more background. If no business owner is an entity, pass in an
              empty list. However, either this parameter or `beneficial_owner_individuals`
              must be populated. on entities that should be included.

          beneficial_owner_individuals: List of all direct and indirect individuals with >25% ownership in the company.
              If no entity or individual owns >25% of the company, and the largest shareholder
              is an individual, please identify them in this field. See
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

          external_id: A user provided id that can be used to link an account holder with an external
              system

          kyb_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          website_url: Company website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        individual: account_holder_create_params.KYCIndividual,
        tos_timestamp: str,
        workflow: Literal["KYC_BASIC", "KYC_BYO"],
        external_id: str | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Create an account holder and initiate the appropriate onboarding workflow.
        Account holders and accounts have a 1:1 relationship. When an account holder is
        successfully created an associated account is also created. All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the enrollment is under review or further action will be needed to
        complete the account enrollment process. This endpoint can only be used on
        accounts that are part of the program that the calling API key manages.

        Args:
          individual: Information on individual for whom the account is being opened and KYC is being
              run.

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYC workflow to run.

          external_id: A user provided id that can be used to link an account holder with an external
              system

          kyc_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        address: Address,
        email: str,
        first_name: str,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"],
        last_name: str,
        phone_number: str,
        workflow: Literal["KYC_EXEMPT"],
        business_account_token: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Create an account holder and initiate the appropriate onboarding workflow.
        Account holders and accounts have a 1:1 relationship. When an account holder is
        successfully created an associated account is also created. All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the enrollment is under review or further action will be needed to
        complete the account enrollment process. This endpoint can only be used on
        accounts that are part of the program that the calling API key manages.

        Args:
          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable.

          email: The KYC Exempt user's email

          first_name: The KYC Exempt user's first name

          kyc_exemption_type: Specifies the type of KYC Exempt user

          last_name: The KYC Exempt user's last name

          phone_number: The KYC Exempt user's phone number, entered in E.164 format.

          workflow: Specifies the workflow type. This must be 'KYC_EXEMPT'

          business_account_token: Only applicable for customers using the KYC-Exempt workflow to enroll authorized
              users of businesses. Pass the account_token of the enrolled business associated
              with the AUTHORIZED_USER in this field.

          external_id: A user provided id that can be used to link an account holder with an external
              system

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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
        ["address", "email", "first_name", "kyc_exemption_type", "last_name", "phone_number", "workflow"],
    )
    def create(
        self,
        *,
        beneficial_owner_entities: Iterable[account_holder_create_params.KYBBeneficialOwnerEntity]
        | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: Iterable[account_holder_create_params.KYBBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_create_params.KYBBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_create_params.KYBControlPerson | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str | NotGiven = NOT_GIVEN,
        workflow: Literal["KYB_BASIC", "KYB_BYO"] | Literal["KYC_BASIC", "KYC_BYO"] | Literal["KYC_EXEMPT"],
        external_id: str | NotGiven = NOT_GIVEN,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        individual: account_holder_create_params.KYCIndividual | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        address: Address | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        return self._post(
            "/v1/account_holders",
            body=maybe_transform(
                {
                    "beneficial_owner_entities": beneficial_owner_entities,
                    "beneficial_owner_individuals": beneficial_owner_individuals,
                    "business_entity": business_entity,
                    "control_person": control_person,
                    "nature_of_business": nature_of_business,
                    "tos_timestamp": tos_timestamp,
                    "workflow": workflow,
                    "external_id": external_id,
                    "kyb_passed_timestamp": kyb_passed_timestamp,
                    "website_url": website_url,
                    "individual": individual,
                    "kyc_passed_timestamp": kyc_passed_timestamp,
                    "address": address,
                    "email": email,
                    "first_name": first_name,
                    "kyc_exemption_type": kyc_exemption_type,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "business_account_token": business_account_token,
                },
                account_holder_create_params.AccountHolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderCreateResponse,
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
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return self._get(
            f"/v1/account_holders/{account_holder_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolder,
        )

    @overload
    def update(
        self,
        account_holder_token: str,
        *,
        beneficial_owner_entities: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerEntity]
        | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_update_params.KYBPatchRequestBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_update_params.KYBPatchRequestControlPerson | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder (including
        business owners and control persons associated to a business account). If Lithic
        is performing KYB or KYC and additional verification is required we will run the
        individual's or business's updated information again and return whether the
        status is accepted or pending (i.e., further action required). All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the workflow is under review or further action will be needed to
        complete the evaluation process. This endpoint can only be used on existing
        accounts that are part of the program that the calling API key manages.

        Args:
          beneficial_owner_entities: List of all entities with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an entity,
              please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)(Section
              I) for more background. If no business owner is an entity, pass in an empty
              list. However, either this parameter or `beneficial_owner_individuals` must be
              populated. on entities that should be included.

          beneficial_owner_individuals: List of all individuals with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an
              individual, please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)(Section
              I) for more background on individuals that should be included. If no individual
              is an entity, pass in an empty list. However, either this parameter or
              `beneficial_owner_entities` must be populated.

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

          external_id: A user provided id that can be used to link an account holder with an external
              system

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          website_url: Company website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        account_holder_token: str,
        *,
        external_id: str | NotGiven = NOT_GIVEN,
        individual: account_holder_update_params.KYCPatchRequestIndividual | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder (including
        business owners and control persons associated to a business account). If Lithic
        is performing KYB or KYC and additional verification is required we will run the
        individual's or business's updated information again and return whether the
        status is accepted or pending (i.e., further action required). All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the workflow is under review or further action will be needed to
        complete the evaluation process. This endpoint can only be used on existing
        accounts that are part of the program that the calling API key manages.

        Args:
          external_id: A user provided id that can be used to link an account holder with an external
              system

          individual: Information on the individual for whom the account is being opened and KYC is
              being run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        account_holder_token: str,
        *,
        address: AddressUpdateParam | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        legal_business_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder (including
        business owners and control persons associated to a business account). If Lithic
        is performing KYB or KYC and additional verification is required we will run the
        individual's or business's updated information again and return whether the
        status is accepted or pending (i.e., further action required). All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the workflow is under review or further action will be needed to
        complete the evaluation process. This endpoint can only be used on existing
        accounts that are part of the program that the calling API key manages.

        Args:
          address: Allowed for: KYC-Exempt, BYO-KYC, BYO-KYB.

          business_account_token: Allowed for: KYC-Exempt, BYO-KYC. The token of the business account to which the
              account holder is associated.

          email: Allowed for all Account Holders. Account holder's email address. The primary
              purpose of this field is for cardholder identification and verification during
              the digital wallet tokenization process.

          first_name: Allowed for KYC-Exempt, BYO-KYC. Account holder's first name.

          last_name: Allowed for KYC-Exempt, BYO-KYC. Account holder's last name.

          legal_business_name: Allowed for BYO-KYB. Legal business name of the account holder.

          phone_number: Allowed for all Account Holders. Account holder's phone number, entered in E.164
              format. The primary purpose of this field is for cardholder identification and
              verification during the digital wallet tokenization process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        account_holder_token: str,
        *,
        beneficial_owner_entities: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerEntity]
        | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_update_params.KYBPatchRequestBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_update_params.KYBPatchRequestControlPerson | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        individual: account_holder_update_params.KYCPatchRequestIndividual | NotGiven = NOT_GIVEN,
        address: AddressUpdateParam | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        legal_business_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return cast(
            AccountHolderUpdateResponse,
            self._patch(
                f"/v1/account_holders/{account_holder_token}",
                body=maybe_transform(
                    {
                        "beneficial_owner_entities": beneficial_owner_entities,
                        "beneficial_owner_individuals": beneficial_owner_individuals,
                        "business_entity": business_entity,
                        "control_person": control_person,
                        "external_id": external_id,
                        "nature_of_business": nature_of_business,
                        "website_url": website_url,
                        "individual": individual,
                        "address": address,
                        "business_account_token": business_account_token,
                        "email": email,
                        "first_name": first_name,
                        "last_name": last_name,
                        "legal_business_name": legal_business_name,
                        "phone_number": phone_number,
                    },
                    account_holder_update_params.AccountHolderUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AccountHolderUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        legal_business_name: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[AccountHolder]:
        """
        Get a list of individual or business account holders and their KYC or KYB
        evaluation status.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          email: Email address of the account holder. The query must be an exact match, case
              insensitive.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          external_id: If applicable, represents the external_id associated with the account_holder.

          first_name: (Individual Account Holders only) The first name of the account holder. The
              query is case insensitive and supports partial matches.

          last_name: (Individual Account Holders only) The last name of the account holder. The query
              is case insensitive and supports partial matches.

          legal_business_name: (Business Account Holders only) The legal business name of the account holder.
              The query is case insensitive and supports partial matches.

          limit: The number of account_holders to limit the response to.

          phone_number: Phone number of the account holder. The query must be an exact match.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account_holders",
            page=SyncSinglePage[AccountHolder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "email": email,
                        "end": end,
                        "ending_before": ending_before,
                        "external_id": external_id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "legal_business_name": legal_business_name,
                        "limit": limit,
                        "phone_number": phone_number,
                        "starting_after": starting_after,
                    },
                    account_holder_list_params.AccountHolderListParams,
                ),
            ),
            model=AccountHolder,
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
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return self._get(
            f"/v1/account_holders/{account_holder_token}/documents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderListDocumentsResponse,
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
    ) -> Document:
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
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        if not document_token:
            raise ValueError(f"Expected a non-empty value for `document_token` but received {document_token!r}")
        return self._get(
            f"/v1/account_holders/{account_holder_token}/documents/{document_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def simulate_enrollment_document_review(
        self,
        *,
        document_upload_token: str,
        status: Literal["UPLOADED", "ACCEPTED", "REJECTED", "PARTIAL_APPROVAL"],
        accepted_entity_status_reasons: List[str] | NotGiven = NOT_GIVEN,
        status_reason: Literal[
            "DOCUMENT_MISSING_REQUIRED_DATA",
            "DOCUMENT_UPLOAD_TOO_BLURRY",
            "FILE_SIZE_TOO_LARGE",
            "INVALID_DOCUMENT_TYPE",
            "INVALID_DOCUMENT_UPLOAD",
            "INVALID_ENTITY",
            "DOCUMENT_EXPIRED",
            "DOCUMENT_ISSUED_GREATER_THAN_30_DAYS",
            "DOCUMENT_TYPE_NOT_SUPPORTED",
            "UNKNOWN_FAILURE_REASON",
            "UNKNOWN_ERROR",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Simulates a review for an account holder document upload.

        Args:
          document_upload_token: The account holder document upload which to perform the simulation upon.

          status: An account holder document's upload status for use within the simulation.

          accepted_entity_status_reasons: A list of status reasons associated with a KYB account holder in PENDING_REVIEW

          status_reason: Status reason that will be associated with the simulated account holder status.
              Only required for a `REJECTED` status or `PARTIAL_APPROVAL` status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulate/account_holders/enrollment_document_review",
            body=maybe_transform(
                {
                    "document_upload_token": document_upload_token,
                    "status": status,
                    "accepted_entity_status_reasons": accepted_entity_status_reasons,
                    "status_reason": status_reason,
                },
                account_holder_simulate_enrollment_document_review_params.AccountHolderSimulateEnrollmentDocumentReviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    def simulate_enrollment_review(
        self,
        *,
        account_holder_token: str | NotGiven = NOT_GIVEN,
        status: Literal["ACCEPTED", "REJECTED"] | NotGiven = NOT_GIVEN,
        status_reasons: List[
            Literal[
                "PRIMARY_BUSINESS_ENTITY_ID_VERIFICATION_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_ADDRESS_VERIFICATION_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_NAME_VERIFICATION_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_BUSINESS_OFFICERS_NOT_MATCHED",
                "PRIMARY_BUSINESS_ENTITY_SOS_FILING_INACTIVE",
                "PRIMARY_BUSINESS_ENTITY_SOS_NOT_MATCHED",
                "PRIMARY_BUSINESS_ENTITY_CMRA_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_WATCHLIST_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_REGISTERED_AGENT_FAILURE",
                "CONTROL_PERSON_BLOCKLIST_ALERT_FAILURE",
                "CONTROL_PERSON_ID_VERIFICATION_FAILURE",
                "CONTROL_PERSON_DOB_VERIFICATION_FAILURE",
                "CONTROL_PERSON_NAME_VERIFICATION_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_DOB_VERIFICATION_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_BLOCKLIST_ALERT_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_ID_VERIFICATION_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_NAME_VERIFICATION_FAILURE",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderSimulateEnrollmentReviewResponse:
        """Simulates an enrollment review for an account holder.

        This endpoint is only
        applicable for workflows that may required intervention such as `KYB_BASIC`.

        Args:
          account_holder_token: The account holder which to perform the simulation upon.

          status: An account holder's status for use within the simulation.

          status_reasons: Status reason that will be associated with the simulated account holder status.
              Only required for a `REJECTED` status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulate/account_holders/enrollment_review",
            body=maybe_transform(
                {
                    "account_holder_token": account_holder_token,
                    "status": status,
                    "status_reasons": status_reasons,
                },
                account_holder_simulate_enrollment_review_params.AccountHolderSimulateEnrollmentReviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderSimulateEnrollmentReviewResponse,
        )

    def upload_document(
        self,
        account_holder_token: str,
        *,
        document_type: Literal[
            "EIN_LETTER",
            "TAX_RETURN",
            "OPERATING_AGREEMENT",
            "CERTIFICATE_OF_FORMATION",
            "DRIVERS_LICENSE",
            "PASSPORT",
            "PASSPORT_CARD",
            "CERTIFICATE_OF_GOOD_STANDING",
            "ARTICLES_OF_INCORPORATION",
            "ARTICLES_OF_ORGANIZATION",
            "BYLAWS",
            "GOVERNMENT_BUSINESS_LICENSE",
            "PARTNERSHIP_AGREEMENT",
            "SS4_FORM",
            "BANK_STATEMENT",
            "UTILITY_BILL_STATEMENT",
            "SSN_CARD",
            "ITIN_LETTER",
            "FINCEN_BOI_REPORT",
        ],
        entity_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
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
          document_type: The type of document to upload

          entity_token: Globally unique identifier for the entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return self._post(
            f"/v1/account_holders/{account_holder_token}/documents",
            body=maybe_transform(
                {
                    "document_type": document_type,
                    "entity_token": entity_token,
                },
                account_holder_upload_document_params.AccountHolderUploadDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )


class AsyncAccountHolders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountHoldersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountHoldersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountHoldersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncAccountHoldersWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        beneficial_owner_entities: Iterable[account_holder_create_params.KYBBeneficialOwnerEntity],
        beneficial_owner_individuals: Iterable[account_holder_create_params.KYBBeneficialOwnerIndividual],
        business_entity: account_holder_create_params.KYBBusinessEntity,
        control_person: account_holder_create_params.KYBControlPerson,
        nature_of_business: str,
        tos_timestamp: str,
        workflow: Literal["KYB_BASIC", "KYB_BYO"],
        external_id: str | NotGiven = NOT_GIVEN,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Create an account holder and initiate the appropriate onboarding workflow.
        Account holders and accounts have a 1:1 relationship. When an account holder is
        successfully created an associated account is also created. All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the enrollment is under review or further action will be needed to
        complete the account enrollment process. This endpoint can only be used on
        accounts that are part of the program that the calling API key manages.

        Args:
          beneficial_owner_entities: List of all entities with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an entity,
              please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
              (Section I) for more background. If no business owner is an entity, pass in an
              empty list. However, either this parameter or `beneficial_owner_individuals`
              must be populated. on entities that should be included.

          beneficial_owner_individuals: List of all direct and indirect individuals with >25% ownership in the company.
              If no entity or individual owns >25% of the company, and the largest shareholder
              is an individual, please identify them in this field. See
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

          external_id: A user provided id that can be used to link an account holder with an external
              system

          kyb_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              business with a pass result.

              This field is required only if workflow type is `KYB_BYO`.

          website_url: Company website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        individual: account_holder_create_params.KYCIndividual,
        tos_timestamp: str,
        workflow: Literal["KYC_BASIC", "KYC_BYO"],
        external_id: str | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Create an account holder and initiate the appropriate onboarding workflow.
        Account holders and accounts have a 1:1 relationship. When an account holder is
        successfully created an associated account is also created. All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the enrollment is under review or further action will be needed to
        complete the account enrollment process. This endpoint can only be used on
        accounts that are part of the program that the calling API key manages.

        Args:
          individual: Information on individual for whom the account is being opened and KYC is being
              run.

          tos_timestamp: An RFC 3339 timestamp indicating when the account holder accepted the applicable
              legal agreements (e.g., cardholder terms) as agreed upon during API customer's
              implementation with Lithic.

          workflow: Specifies the type of KYC workflow to run.

          external_id: A user provided id that can be used to link an account holder with an external
              system

          kyc_passed_timestamp: An RFC 3339 timestamp indicating when precomputed KYC was completed on the
              individual with a pass result.

              This field is required only if workflow type is `KYC_BYO`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        address: Address,
        email: str,
        first_name: str,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"],
        last_name: str,
        phone_number: str,
        workflow: Literal["KYC_EXEMPT"],
        business_account_token: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        """
        Create an account holder and initiate the appropriate onboarding workflow.
        Account holders and accounts have a 1:1 relationship. When an account holder is
        successfully created an associated account is also created. All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the enrollment is under review or further action will be needed to
        complete the account enrollment process. This endpoint can only be used on
        accounts that are part of the program that the calling API key manages.

        Args:
          address: KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable.

          email: The KYC Exempt user's email

          first_name: The KYC Exempt user's first name

          kyc_exemption_type: Specifies the type of KYC Exempt user

          last_name: The KYC Exempt user's last name

          phone_number: The KYC Exempt user's phone number, entered in E.164 format.

          workflow: Specifies the workflow type. This must be 'KYC_EXEMPT'

          business_account_token: Only applicable for customers using the KYC-Exempt workflow to enroll authorized
              users of businesses. Pass the account_token of the enrolled business associated
              with the AUTHORIZED_USER in this field.

          external_id: A user provided id that can be used to link an account holder with an external
              system

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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
        ["address", "email", "first_name", "kyc_exemption_type", "last_name", "phone_number", "workflow"],
    )
    async def create(
        self,
        *,
        beneficial_owner_entities: Iterable[account_holder_create_params.KYBBeneficialOwnerEntity]
        | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: Iterable[account_holder_create_params.KYBBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_create_params.KYBBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_create_params.KYBControlPerson | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        tos_timestamp: str | NotGiven = NOT_GIVEN,
        workflow: Literal["KYB_BASIC", "KYB_BYO"] | Literal["KYC_BASIC", "KYC_BYO"] | Literal["KYC_EXEMPT"],
        external_id: str | NotGiven = NOT_GIVEN,
        kyb_passed_timestamp: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        individual: account_holder_create_params.KYCIndividual | NotGiven = NOT_GIVEN,
        kyc_passed_timestamp: str | NotGiven = NOT_GIVEN,
        address: Address | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"] | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderCreateResponse:
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        return await self._post(
            "/v1/account_holders",
            body=await async_maybe_transform(
                {
                    "beneficial_owner_entities": beneficial_owner_entities,
                    "beneficial_owner_individuals": beneficial_owner_individuals,
                    "business_entity": business_entity,
                    "control_person": control_person,
                    "nature_of_business": nature_of_business,
                    "tos_timestamp": tos_timestamp,
                    "workflow": workflow,
                    "external_id": external_id,
                    "kyb_passed_timestamp": kyb_passed_timestamp,
                    "website_url": website_url,
                    "individual": individual,
                    "kyc_passed_timestamp": kyc_passed_timestamp,
                    "address": address,
                    "email": email,
                    "first_name": first_name,
                    "kyc_exemption_type": kyc_exemption_type,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "business_account_token": business_account_token,
                },
                account_holder_create_params.AccountHolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderCreateResponse,
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
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return await self._get(
            f"/v1/account_holders/{account_holder_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolder,
        )

    @overload
    async def update(
        self,
        account_holder_token: str,
        *,
        beneficial_owner_entities: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerEntity]
        | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_update_params.KYBPatchRequestBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_update_params.KYBPatchRequestControlPerson | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder (including
        business owners and control persons associated to a business account). If Lithic
        is performing KYB or KYC and additional verification is required we will run the
        individual's or business's updated information again and return whether the
        status is accepted or pending (i.e., further action required). All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the workflow is under review or further action will be needed to
        complete the evaluation process. This endpoint can only be used on existing
        accounts that are part of the program that the calling API key manages.

        Args:
          beneficial_owner_entities: List of all entities with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an entity,
              please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)(Section
              I) for more background. If no business owner is an entity, pass in an empty
              list. However, either this parameter or `beneficial_owner_individuals` must be
              populated. on entities that should be included.

          beneficial_owner_individuals: List of all individuals with >25% ownership in the company. If no entity or
              individual owns >25% of the company, and the largest shareholder is an
              individual, please identify them in this field. See
              [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)(Section
              I) for more background on individuals that should be included. If no individual
              is an entity, pass in an empty list. However, either this parameter or
              `beneficial_owner_entities` must be populated.

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

          external_id: A user provided id that can be used to link an account holder with an external
              system

          nature_of_business: Short description of the company's line of business (i.e., what does the company
              do?).

          website_url: Company website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        account_holder_token: str,
        *,
        external_id: str | NotGiven = NOT_GIVEN,
        individual: account_holder_update_params.KYCPatchRequestIndividual | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder (including
        business owners and control persons associated to a business account). If Lithic
        is performing KYB or KYC and additional verification is required we will run the
        individual's or business's updated information again and return whether the
        status is accepted or pending (i.e., further action required). All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the workflow is under review or further action will be needed to
        complete the evaluation process. This endpoint can only be used on existing
        accounts that are part of the program that the calling API key manages.

        Args:
          external_id: A user provided id that can be used to link an account holder with an external
              system

          individual: Information on the individual for whom the account is being opened and KYC is
              being run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        account_holder_token: str,
        *,
        address: AddressUpdateParam | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        legal_business_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        """
        Update the information associated with a particular account holder (including
        business owners and control persons associated to a business account). If Lithic
        is performing KYB or KYC and additional verification is required we will run the
        individual's or business's updated information again and return whether the
        status is accepted or pending (i.e., further action required). All calls to this
        endpoint will return an immediate response - though in some cases, the response
        may indicate the workflow is under review or further action will be needed to
        complete the evaluation process. This endpoint can only be used on existing
        accounts that are part of the program that the calling API key manages.

        Args:
          address: Allowed for: KYC-Exempt, BYO-KYC, BYO-KYB.

          business_account_token: Allowed for: KYC-Exempt, BYO-KYC. The token of the business account to which the
              account holder is associated.

          email: Allowed for all Account Holders. Account holder's email address. The primary
              purpose of this field is for cardholder identification and verification during
              the digital wallet tokenization process.

          first_name: Allowed for KYC-Exempt, BYO-KYC. Account holder's first name.

          last_name: Allowed for KYC-Exempt, BYO-KYC. Account holder's last name.

          legal_business_name: Allowed for BYO-KYB. Legal business name of the account holder.

          phone_number: Allowed for all Account Holders. Account holder's phone number, entered in E.164
              format. The primary purpose of this field is for cardholder identification and
              verification during the digital wallet tokenization process.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        account_holder_token: str,
        *,
        beneficial_owner_entities: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerEntity]
        | NotGiven = NOT_GIVEN,
        beneficial_owner_individuals: Iterable[account_holder_update_params.KYBPatchRequestBeneficialOwnerIndividual]
        | NotGiven = NOT_GIVEN,
        business_entity: account_holder_update_params.KYBPatchRequestBusinessEntity | NotGiven = NOT_GIVEN,
        control_person: account_holder_update_params.KYBPatchRequestControlPerson | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        nature_of_business: str | NotGiven = NOT_GIVEN,
        website_url: str | NotGiven = NOT_GIVEN,
        individual: account_holder_update_params.KYCPatchRequestIndividual | NotGiven = NOT_GIVEN,
        address: AddressUpdateParam | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        legal_business_name: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderUpdateResponse:
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return cast(
            AccountHolderUpdateResponse,
            await self._patch(
                f"/v1/account_holders/{account_holder_token}",
                body=await async_maybe_transform(
                    {
                        "beneficial_owner_entities": beneficial_owner_entities,
                        "beneficial_owner_individuals": beneficial_owner_individuals,
                        "business_entity": business_entity,
                        "control_person": control_person,
                        "external_id": external_id,
                        "nature_of_business": nature_of_business,
                        "website_url": website_url,
                        "individual": individual,
                        "address": address,
                        "business_account_token": business_account_token,
                        "email": email,
                        "first_name": first_name,
                        "last_name": last_name,
                        "legal_business_name": legal_business_name,
                        "phone_number": phone_number,
                    },
                    account_holder_update_params.AccountHolderUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AccountHolderUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        legal_business_name: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountHolder, AsyncSinglePage[AccountHolder]]:
        """
        Get a list of individual or business account holders and their KYC or KYB
        evaluation status.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          email: Email address of the account holder. The query must be an exact match, case
              insensitive.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          external_id: If applicable, represents the external_id associated with the account_holder.

          first_name: (Individual Account Holders only) The first name of the account holder. The
              query is case insensitive and supports partial matches.

          last_name: (Individual Account Holders only) The last name of the account holder. The query
              is case insensitive and supports partial matches.

          legal_business_name: (Business Account Holders only) The legal business name of the account holder.
              The query is case insensitive and supports partial matches.

          limit: The number of account_holders to limit the response to.

          phone_number: Phone number of the account holder. The query must be an exact match.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account_holders",
            page=AsyncSinglePage[AccountHolder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "email": email,
                        "end": end,
                        "ending_before": ending_before,
                        "external_id": external_id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "legal_business_name": legal_business_name,
                        "limit": limit,
                        "phone_number": phone_number,
                        "starting_after": starting_after,
                    },
                    account_holder_list_params.AccountHolderListParams,
                ),
            ),
            model=AccountHolder,
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
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return await self._get(
            f"/v1/account_holders/{account_holder_token}/documents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderListDocumentsResponse,
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
    ) -> Document:
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
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        if not document_token:
            raise ValueError(f"Expected a non-empty value for `document_token` but received {document_token!r}")
        return await self._get(
            f"/v1/account_holders/{account_holder_token}/documents/{document_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    async def simulate_enrollment_document_review(
        self,
        *,
        document_upload_token: str,
        status: Literal["UPLOADED", "ACCEPTED", "REJECTED", "PARTIAL_APPROVAL"],
        accepted_entity_status_reasons: List[str] | NotGiven = NOT_GIVEN,
        status_reason: Literal[
            "DOCUMENT_MISSING_REQUIRED_DATA",
            "DOCUMENT_UPLOAD_TOO_BLURRY",
            "FILE_SIZE_TOO_LARGE",
            "INVALID_DOCUMENT_TYPE",
            "INVALID_DOCUMENT_UPLOAD",
            "INVALID_ENTITY",
            "DOCUMENT_EXPIRED",
            "DOCUMENT_ISSUED_GREATER_THAN_30_DAYS",
            "DOCUMENT_TYPE_NOT_SUPPORTED",
            "UNKNOWN_FAILURE_REASON",
            "UNKNOWN_ERROR",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
        """
        Simulates a review for an account holder document upload.

        Args:
          document_upload_token: The account holder document upload which to perform the simulation upon.

          status: An account holder document's upload status for use within the simulation.

          accepted_entity_status_reasons: A list of status reasons associated with a KYB account holder in PENDING_REVIEW

          status_reason: Status reason that will be associated with the simulated account holder status.
              Only required for a `REJECTED` status or `PARTIAL_APPROVAL` status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulate/account_holders/enrollment_document_review",
            body=await async_maybe_transform(
                {
                    "document_upload_token": document_upload_token,
                    "status": status,
                    "accepted_entity_status_reasons": accepted_entity_status_reasons,
                    "status_reason": status_reason,
                },
                account_holder_simulate_enrollment_document_review_params.AccountHolderSimulateEnrollmentDocumentReviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )

    async def simulate_enrollment_review(
        self,
        *,
        account_holder_token: str | NotGiven = NOT_GIVEN,
        status: Literal["ACCEPTED", "REJECTED"] | NotGiven = NOT_GIVEN,
        status_reasons: List[
            Literal[
                "PRIMARY_BUSINESS_ENTITY_ID_VERIFICATION_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_ADDRESS_VERIFICATION_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_NAME_VERIFICATION_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_BUSINESS_OFFICERS_NOT_MATCHED",
                "PRIMARY_BUSINESS_ENTITY_SOS_FILING_INACTIVE",
                "PRIMARY_BUSINESS_ENTITY_SOS_NOT_MATCHED",
                "PRIMARY_BUSINESS_ENTITY_CMRA_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_WATCHLIST_FAILURE",
                "PRIMARY_BUSINESS_ENTITY_REGISTERED_AGENT_FAILURE",
                "CONTROL_PERSON_BLOCKLIST_ALERT_FAILURE",
                "CONTROL_PERSON_ID_VERIFICATION_FAILURE",
                "CONTROL_PERSON_DOB_VERIFICATION_FAILURE",
                "CONTROL_PERSON_NAME_VERIFICATION_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_DOB_VERIFICATION_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_BLOCKLIST_ALERT_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_ID_VERIFICATION_FAILURE",
                "BENEFICIAL_OWNER_INDIVIDUAL_NAME_VERIFICATION_FAILURE",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountHolderSimulateEnrollmentReviewResponse:
        """Simulates an enrollment review for an account holder.

        This endpoint is only
        applicable for workflows that may required intervention such as `KYB_BASIC`.

        Args:
          account_holder_token: The account holder which to perform the simulation upon.

          status: An account holder's status for use within the simulation.

          status_reasons: Status reason that will be associated with the simulated account holder status.
              Only required for a `REJECTED` status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulate/account_holders/enrollment_review",
            body=await async_maybe_transform(
                {
                    "account_holder_token": account_holder_token,
                    "status": status,
                    "status_reasons": status_reasons,
                },
                account_holder_simulate_enrollment_review_params.AccountHolderSimulateEnrollmentReviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderSimulateEnrollmentReviewResponse,
        )

    async def upload_document(
        self,
        account_holder_token: str,
        *,
        document_type: Literal[
            "EIN_LETTER",
            "TAX_RETURN",
            "OPERATING_AGREEMENT",
            "CERTIFICATE_OF_FORMATION",
            "DRIVERS_LICENSE",
            "PASSPORT",
            "PASSPORT_CARD",
            "CERTIFICATE_OF_GOOD_STANDING",
            "ARTICLES_OF_INCORPORATION",
            "ARTICLES_OF_ORGANIZATION",
            "BYLAWS",
            "GOVERNMENT_BUSINESS_LICENSE",
            "PARTNERSHIP_AGREEMENT",
            "SS4_FORM",
            "BANK_STATEMENT",
            "UTILITY_BILL_STATEMENT",
            "SSN_CARD",
            "ITIN_LETTER",
            "FINCEN_BOI_REPORT",
        ],
        entity_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Document:
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
          document_type: The type of document to upload

          entity_token: Globally unique identifier for the entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return await self._post(
            f"/v1/account_holders/{account_holder_token}/documents",
            body=await async_maybe_transform(
                {
                    "document_type": document_type,
                    "entity_token": entity_token,
                },
                account_holder_upload_document_params.AccountHolderUploadDocumentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Document,
        )


class AccountHoldersWithRawResponse:
    def __init__(self, account_holders: AccountHolders) -> None:
        self._account_holders = account_holders

        self.create = _legacy_response.to_raw_response_wrapper(
            account_holders.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            account_holders.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            account_holders.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            account_holders.list,
        )
        self.list_documents = _legacy_response.to_raw_response_wrapper(
            account_holders.list_documents,
        )
        self.retrieve_document = _legacy_response.to_raw_response_wrapper(
            account_holders.retrieve_document,
        )
        self.simulate_enrollment_document_review = _legacy_response.to_raw_response_wrapper(
            account_holders.simulate_enrollment_document_review,
        )
        self.simulate_enrollment_review = _legacy_response.to_raw_response_wrapper(
            account_holders.simulate_enrollment_review,
        )
        self.upload_document = _legacy_response.to_raw_response_wrapper(
            account_holders.upload_document,
        )


class AsyncAccountHoldersWithRawResponse:
    def __init__(self, account_holders: AsyncAccountHolders) -> None:
        self._account_holders = account_holders

        self.create = _legacy_response.async_to_raw_response_wrapper(
            account_holders.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            account_holders.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            account_holders.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            account_holders.list,
        )
        self.list_documents = _legacy_response.async_to_raw_response_wrapper(
            account_holders.list_documents,
        )
        self.retrieve_document = _legacy_response.async_to_raw_response_wrapper(
            account_holders.retrieve_document,
        )
        self.simulate_enrollment_document_review = _legacy_response.async_to_raw_response_wrapper(
            account_holders.simulate_enrollment_document_review,
        )
        self.simulate_enrollment_review = _legacy_response.async_to_raw_response_wrapper(
            account_holders.simulate_enrollment_review,
        )
        self.upload_document = _legacy_response.async_to_raw_response_wrapper(
            account_holders.upload_document,
        )


class AccountHoldersWithStreamingResponse:
    def __init__(self, account_holders: AccountHolders) -> None:
        self._account_holders = account_holders

        self.create = to_streamed_response_wrapper(
            account_holders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_holders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            account_holders.update,
        )
        self.list = to_streamed_response_wrapper(
            account_holders.list,
        )
        self.list_documents = to_streamed_response_wrapper(
            account_holders.list_documents,
        )
        self.retrieve_document = to_streamed_response_wrapper(
            account_holders.retrieve_document,
        )
        self.simulate_enrollment_document_review = to_streamed_response_wrapper(
            account_holders.simulate_enrollment_document_review,
        )
        self.simulate_enrollment_review = to_streamed_response_wrapper(
            account_holders.simulate_enrollment_review,
        )
        self.upload_document = to_streamed_response_wrapper(
            account_holders.upload_document,
        )


class AsyncAccountHoldersWithStreamingResponse:
    def __init__(self, account_holders: AsyncAccountHolders) -> None:
        self._account_holders = account_holders

        self.create = async_to_streamed_response_wrapper(
            account_holders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_holders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            account_holders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            account_holders.list,
        )
        self.list_documents = async_to_streamed_response_wrapper(
            account_holders.list_documents,
        )
        self.retrieve_document = async_to_streamed_response_wrapper(
            account_holders.retrieve_document,
        )
        self.simulate_enrollment_document_review = async_to_streamed_response_wrapper(
            account_holders.simulate_enrollment_document_review,
        )
        self.simulate_enrollment_review = async_to_streamed_response_wrapper(
            account_holders.simulate_enrollment_review,
        )
        self.upload_document = async_to_streamed_response_wrapper(
            account_holders.upload_document,
        )
