# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .required_document import RequiredDocument
from .kyb_business_entity import KYBBusinessEntity

__all__ = [
    "AccountHolderUpdateResponse",
    "KYBKYCPatchResponse",
    "KybkycPatchResponseBeneficialOwnerIndividual",
    "KybkycPatchResponseBeneficialOwnerIndividualAddress",
    "KYBKYCPatchResponseControlPerson",
    "KYBKYCPatchResponseControlPersonAddress",
    "KYBKYCPatchResponseIndividual",
    "KYBKYCPatchResponseIndividualAddress",
    "KYBKYCPatchResponseVerificationApplication",
    "PatchResponse",
    "PatchResponseAddress",
]


class KybkycPatchResponseBeneficialOwnerIndividualAddress(BaseModel):
    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class KybkycPatchResponseBeneficialOwnerIndividual(BaseModel):
    address: Optional[KybkycPatchResponseBeneficialOwnerIndividualAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date."""

    email: Optional[str] = None
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format."""


class KYBKYCPatchResponseControlPersonAddress(BaseModel):
    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class KYBKYCPatchResponseControlPerson(BaseModel):
    address: Optional[KYBKYCPatchResponseControlPersonAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date."""

    email: Optional[str] = None
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format."""


class KYBKYCPatchResponseIndividualAddress(BaseModel):
    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class KYBKYCPatchResponseIndividual(BaseModel):
    address: Optional[KYBKYCPatchResponseIndividualAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date."""

    email: Optional[str] = None
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format."""


class KYBKYCPatchResponseVerificationApplication(BaseModel):
    created: datetime
    """Timestamp of when the application was created."""

    status: Literal["ACCEPTED", "PENDING_DOCUMENT", "PENDING_RESUBMIT", "REJECTED"]
    """KYC and KYB evaluation states.

    Note: `PENDING_RESUBMIT` and `PENDING_DOCUMENT` are only applicable for the
    `ADVANCED` workflow.
    """

    status_reasons: List[
        Literal[
            "ADDRESS_VERIFICATION_FAILURE",
            "AGE_THRESHOLD_FAILURE",
            "COMPLETE_VERIFICATION_FAILURE",
            "DOB_VERIFICATION_FAILURE",
            "ID_VERIFICATION_FAILURE",
            "MAX_DOCUMENT_ATTEMPTS",
            "MAX_RESUBMISSION_ATTEMPTS",
            "NAME_VERIFICATION_FAILURE",
            "OTHER_VERIFICATION_FAILURE",
            "RISK_THRESHOLD_FAILURE",
            "WATCHLIST_ALERT_FAILURE",
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
        ]
    ]
    """Reason for the evaluation status."""

    updated: datetime
    """Timestamp of when the application was last updated."""


class KYBKYCPatchResponse(BaseModel):
    token: Optional[str] = None
    """Globally unique identifier for the account holder."""

    account_token: Optional[str] = None
    """Globally unique identifier for the account."""

    beneficial_owner_entities: Optional[List[KYBBusinessEntity]] = None
    """Only present when user_type == "BUSINESS".

    List of all entities with >25% ownership in the company.
    """

    beneficial_owner_individuals: Optional[List[KybkycPatchResponseBeneficialOwnerIndividual]] = None
    """Only present when user_type == "BUSINESS".

    List of all individuals with >25% ownership in the company.
    """

    business_account_token: Optional[str] = None
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Pass the account_token of the enrolled business associated
    with the AUTHORIZED_USER in this field.
    """

    business_entity: Optional[KYBBusinessEntity] = None
    """Only present when user_type == "BUSINESS".

    Information about the business for which the account is being opened and KYB is
    being run.
    """

    control_person: Optional[KYBKYCPatchResponseControlPerson] = None
    """Only present when user_type == "BUSINESS".

    An individual with significant responsibility for managing the legal entity
    (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
    Officer,

    Managing Member, General Partner, President, Vice President, or Treasurer). This
    can be an executive, or someone who will have program-wide access

    to the cards that Lithic will provide. In some cases, this individual could also
    be a beneficial owner listed above.
    """

    created: Optional[datetime] = None
    """Timestamp of when the account holder was created."""

    email: Optional[str] = None
    """
    < Deprecated. Use control_person.email when user_type == "BUSINESS". Use
    individual.phone_number when user_type == "INDIVIDUAL".

    > Primary email of Account Holder.
    """

    exemption_type: Optional[Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"]] = None
    """The type of KYC exemption for a KYC-Exempt Account Holder.

    "None" if the account holder is not KYC-Exempt.
    """

    external_id: Optional[str] = None
    """
    Customer-provided token that indicates a relationship with an object outside of
    the Lithic ecosystem.
    """

    individual: Optional[KYBKYCPatchResponseIndividual] = None
    """Only present when user_type == "INDIVIDUAL".

    Information about the individual for which the account is being opened and KYC
    is being run.
    """

    nature_of_business: Optional[str] = None
    """Only present when user_type == "BUSINESS".

    User-submitted description of the business.
    """

    phone_number: Optional[str] = None
    """
    < Deprecated. Use control_person.phone_number when user_type == "BUSINESS". Use
    individual.phone_number when user_type == "INDIVIDUAL".

    > Primary phone of Account Holder, entered in E.164 format.
    """

    required_documents: Optional[List[RequiredDocument]] = None
    """Only present for "KYB_BASIC" and "KYC_ADVANCED" workflows.

    A list of documents required for the account holder to be approved.
    """

    status: Optional[Literal["ACCEPTED", "PENDING_DOCUMENT", "PENDING_RESUBMIT", "REJECTED"]] = None
    """<Deprecated. Use verification_application.status instead>

    KYC and KYB evaluation states.

    Note: `PENDING_RESUBMIT` and `PENDING_DOCUMENT` are only applicable for the
    `ADVANCED` workflow.
    """

    status_reasons: Optional[
        List[
            Literal[
                "ADDRESS_VERIFICATION_FAILURE",
                "AGE_THRESHOLD_FAILURE",
                "COMPLETE_VERIFICATION_FAILURE",
                "DOB_VERIFICATION_FAILURE",
                "ID_VERIFICATION_FAILURE",
                "MAX_DOCUMENT_ATTEMPTS",
                "MAX_RESUBMISSION_ATTEMPTS",
                "NAME_VERIFICATION_FAILURE",
                "OTHER_VERIFICATION_FAILURE",
                "RISK_THRESHOLD_FAILURE",
                "WATCHLIST_ALERT_FAILURE",
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
            ]
        ]
    ] = None
    """<Deprecated.

    Use verification_application.status_reasons> Reason for the evaluation status.
    """

    user_type: Optional[Literal["BUSINESS", "INDIVIDUAL"]] = None
    """The type of Account Holder.

    If the type is "INDIVIDUAL", the "individual" attribute will be present.

    If the type is "BUSINESS" then the "business_entity", "control_person",
    "beneficial_owner_individuals", "beneficial_owner_entities",

    "nature_of_business", and "website_url" attributes will be present.
    """

    verification_application: Optional[KYBKYCPatchResponseVerificationApplication] = None
    """Information about the most recent identity verification attempt"""

    website_url: Optional[str] = None
    """Only present when user_type == "BUSINESS". Business's primary website."""


class PatchResponseAddress(BaseModel):
    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class PatchResponse(BaseModel):
    token: Optional[str] = None
    """The token for the account holder that was updated"""

    address: Optional[PatchResponseAddress] = None
    """The address for the account holder"""

    business_account_token: Optional[str] = None
    """The token for the business account that the account holder is associated with"""

    email: Optional[str] = None
    """The email for the account holder"""

    first_name: Optional[str] = None
    """The first name for the account holder"""

    last_name: Optional[str] = None
    """The last name for the account holder"""

    legal_business_name: Optional[str] = None
    """The legal business name for the account holder"""

    phone_number: Optional[str] = None
    """The phone_number for the account holder"""


AccountHolderUpdateResponse: TypeAlias = Union[KYBKYCPatchResponse, PatchResponse]
