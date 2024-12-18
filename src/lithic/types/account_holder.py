# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.address import Address
from .required_document import RequiredDocument

__all__ = [
    "AccountHolder",
    "BeneficialOwnerEntity",
    "BeneficialOwnerIndividual",
    "BusinessEntity",
    "ControlPerson",
    "Individual",
    "VerificationApplication",
]


class BeneficialOwnerEntity(BaseModel):
    address: Address
    """
    Business's physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    dba_business_name: str
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    entity_token: str
    """Globally unique identifier for the entity."""

    government_id: str
    """Government-issued identification number.

    US Federal Employer Identification Numbers (EIN) are currently supported,
    entered as full nine-digits, with or without hyphens.
    """

    legal_business_name: str
    """Legal (formal) business name."""

    phone_numbers: List[str]
    """
    One or more of the business's phone number(s), entered as a list in E.164
    format.
    """

    parent_company: Optional[str] = None
    """Parent company name (if applicable)."""


class BeneficialOwnerIndividual(BaseModel):
    address: Address
    """Individual's current address"""

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """Individual's email address."""

    entity_token: str
    """Globally unique identifier for the entity."""

    first_name: str
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: str
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: str
    """Individual's phone number, entered in E.164 format."""


class BusinessEntity(BaseModel):
    address: Address
    """
    Business's physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    dba_business_name: str
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    entity_token: str
    """Globally unique identifier for the entity."""

    government_id: str
    """Government-issued identification number.

    US Federal Employer Identification Numbers (EIN) are currently supported,
    entered as full nine-digits, with or without hyphens.
    """

    legal_business_name: str
    """Legal (formal) business name."""

    phone_numbers: List[str]
    """
    One or more of the business's phone number(s), entered as a list in E.164
    format.
    """

    parent_company: Optional[str] = None
    """Parent company name (if applicable)."""


class ControlPerson(BaseModel):
    address: Address
    """Individual's current address"""

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """Individual's email address."""

    entity_token: str
    """Globally unique identifier for the entity."""

    first_name: str
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: str
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: str
    """Individual's phone number, entered in E.164 format."""


class Individual(BaseModel):
    address: Address
    """Individual's current address"""

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """Individual's email address."""

    entity_token: str
    """Globally unique identifier for the entity."""

    first_name: str
    """Individual's first name, as it appears on government-issued identity documents."""

    last_name: str
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: str
    """Individual's phone number, entered in E.164 format."""


class VerificationApplication(BaseModel):
    created: Optional[datetime] = None
    """Timestamp of when the application was created."""

    status: Optional[Literal["ACCEPTED", "PENDING_REVIEW", "PENDING_DOCUMENT", "PENDING_RESUBMIT", "REJECTED"]] = None
    """KYC and KYB evaluation states.

    Note:

    - `PENDING_REVIEW` is only applicable for the `KYB_BASIC` workflow.
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
            ]
        ]
    ] = None
    """Reason for the evaluation status."""

    updated: Optional[datetime] = None
    """Timestamp of when the application was last updated."""


class AccountHolder(BaseModel):
    token: str
    """Globally unique identifier for the account holder."""

    created: datetime
    """Timestamp of when the account holder was created."""

    account_token: Optional[str] = None
    """Globally unique identifier for the account."""

    beneficial_owner_entities: Optional[List[BeneficialOwnerEntity]] = None
    """Only present when user_type == "BUSINESS".

    List of all entities with >25% ownership in the company.
    """

    beneficial_owner_individuals: Optional[List[BeneficialOwnerIndividual]] = None
    """Only present when user_type == "BUSINESS".

    List of all individuals with >25% ownership in the company.
    """

    business_account_token: Optional[str] = None
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Pass the account_token of the enrolled business associated
    with the AUTHORIZED_USER in this field.
    """

    business_entity: Optional[BusinessEntity] = None
    """Only present when user_type == "BUSINESS".

    Information about the business for which the account is being opened and KYB is
    being run.
    """

    control_person: Optional[ControlPerson] = None
    """
    Only present when user_type == "BUSINESS". An individual with significant
    responsibility for managing the legal entity (e.g., a Chief Executive Officer,
    Chief Financial Officer, Chief Operating Officer, Managing Member, General
    Partner, President, Vice President, or Treasurer). This can be an executive, or
    someone who will have program-wide access to the cards that Lithic will provide.
    In some cases, this individual could also be a beneficial owner listed above.
    """

    email: Optional[str] = None
    """
    < Deprecated. Use control_person.email when user_type == "BUSINESS". Use
    individual.phone_number when user_type == "INDIVIDUAL".

    > Primary email of Account Holder.
    """

    exemption_type: Optional[Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"]] = None
    """The type of KYC exemption for a KYC-Exempt Account Holder."""

    external_id: Optional[str] = None
    """
    Customer-provided token that indicates a relationship with an object outside of
    the Lithic ecosystem.
    """

    individual: Optional[Individual] = None
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
    """Only present for "KYB_BASIC" workflow.

    A list of documents required for the account holder to be approved.
    """

    status: Optional[Literal["ACCEPTED", "PENDING_REVIEW", "PENDING_DOCUMENT", "PENDING_RESUBMIT", "REJECTED"]] = None
    """<Deprecated. Use verification_application.status instead>

    KYC and KYB evaluation states.

    Note:

    - `PENDING_REVIEW` is only applicable for the `KYB_BASIC` workflow.
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
            ]
        ]
    ] = None
    """<Deprecated.

    Use verification_application.status_reasons> Reason for the evaluation status.
    """

    user_type: Optional[Literal["BUSINESS", "INDIVIDUAL"]] = None
    """The type of Account Holder.

    If the type is "INDIVIDUAL", the "individual" attribute will be present. If the
    type is "BUSINESS" then the "business_entity", "control_person",
    "beneficial_owner_individuals", "beneficial_owner_entities",
    "nature_of_business", and "website_url" attributes will be present.
    """

    verification_application: Optional[VerificationApplication] = None
    """Information about the most recent identity verification attempt"""

    website_url: Optional[str] = None
    """Only present when user_type == "BUSINESS". Business's primary website."""
