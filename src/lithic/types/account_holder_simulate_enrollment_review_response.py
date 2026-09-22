# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .required_document import RequiredDocument
from .kyb_business_entity import KYBBusinessEntity

__all__ = [
    "AccountHolderSimulateEnrollmentReviewResponse",
    "BeneficialOwnerIndividual",
    "BeneficialOwnerIndividualAddress",
    "ControlPerson",
    "ControlPersonAddress",
    "Individual",
    "IndividualAddress",
    "VerificationApplication",
]


class BeneficialOwnerIndividualAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB and KYC workflows.
    """

    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """
    Valid country code, entered in uppercase ISO 3166-1 alpha-3 three-character
    format. Supported countries depend on the onboarding workflow used for the
    account holder.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""

    postal_code: Optional[str] = None
    """Valid postal code.

    For USA addresses, enter either a five-digit postal code or a nine-digit postal
    code (ZIP+4) using the format 12345-1234. Required for all countries except the
    following, which do not use postal codes: ABW, AGO, ARE, ATG, BDI, BEN, BFA,
    BHS, BLZ, BOL, BWA, CIV, CMR, COD, COG, COK, COM, DJI, DMA, ERI, FJI, GAB, GMB,
    GNQ, GRD, GUY, HKG, KIR, MAC, MLI, MRT, NIU, NRU, QAT, RWA, SLB, SLE, SSD, SUR,
    SXM, SYC, TGO, TKL, TLS, TON, TUV, UGA, VUT, YEM, ZWE
    """

    state: Optional[str] = None
    """
    Valid state, province, or subdivision code, entered as the uppercase ISO 3166-2
    code for the country without the country prefix. For example, `CA` for
    California. Optional unless the address is in one of the following countries,
    where it is required:

    - `USA`
    - `CAN`
    - `AUS`
    - `CHN`
    - `KOR`
    - `MEX`
    - `MYS`
    - `NZL`
    """


class BeneficialOwnerIndividual(BaseModel):
    address: Optional[BeneficialOwnerIndividualAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB
    and KYC workflows.
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


class ControlPersonAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB and KYC workflows.
    """

    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """
    Valid country code, entered in uppercase ISO 3166-1 alpha-3 three-character
    format. Supported countries depend on the onboarding workflow used for the
    account holder.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""

    postal_code: Optional[str] = None
    """Valid postal code.

    For USA addresses, enter either a five-digit postal code or a nine-digit postal
    code (ZIP+4) using the format 12345-1234. Required for all countries except the
    following, which do not use postal codes: ABW, AGO, ARE, ATG, BDI, BEN, BFA,
    BHS, BLZ, BOL, BWA, CIV, CMR, COD, COG, COK, COM, DJI, DMA, ERI, FJI, GAB, GMB,
    GNQ, GRD, GUY, HKG, KIR, MAC, MLI, MRT, NIU, NRU, QAT, RWA, SLB, SLE, SSD, SUR,
    SXM, SYC, TGO, TKL, TLS, TON, TUV, UGA, VUT, YEM, ZWE
    """

    state: Optional[str] = None
    """
    Valid state, province, or subdivision code, entered as the uppercase ISO 3166-2
    code for the country without the country prefix. For example, `CA` for
    California. Optional unless the address is in one of the following countries,
    where it is required:

    - `USA`
    - `CAN`
    - `AUS`
    - `CHN`
    - `KOR`
    - `MEX`
    - `MYS`
    - `NZL`
    """


class ControlPerson(BaseModel):
    """Only present when user_type == "BUSINESS".

    An individual with significant responsibility for managing the legal entity (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating Officer,

    Managing Member, General Partner, President, Vice President, or Treasurer). This can be an executive, or someone who will have program-wide access

    to the cards that Lithic will provide. In some cases, this individual could also be a beneficial owner listed above.
    """

    address: Optional[ControlPersonAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB
    and KYC workflows.
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


class IndividualAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB and KYC workflows.
    """

    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """
    Valid country code, entered in uppercase ISO 3166-1 alpha-3 three-character
    format. Supported countries depend on the onboarding workflow used for the
    account holder.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""

    postal_code: Optional[str] = None
    """Valid postal code.

    For USA addresses, enter either a five-digit postal code or a nine-digit postal
    code (ZIP+4) using the format 12345-1234. Required for all countries except the
    following, which do not use postal codes: ABW, AGO, ARE, ATG, BDI, BEN, BFA,
    BHS, BLZ, BOL, BWA, CIV, CMR, COD, COG, COK, COM, DJI, DMA, ERI, FJI, GAB, GMB,
    GNQ, GRD, GUY, HKG, KIR, MAC, MLI, MRT, NIU, NRU, QAT, RWA, SLB, SLE, SSD, SUR,
    SXM, SYC, TGO, TKL, TLS, TON, TUV, UGA, VUT, YEM, ZWE
    """

    state: Optional[str] = None
    """
    Valid state, province, or subdivision code, entered as the uppercase ISO 3166-2
    code for the country without the country prefix. For example, `CA` for
    California. Optional unless the address is in one of the following countries,
    where it is required:

    - `USA`
    - `CAN`
    - `AUS`
    - `CHN`
    - `KOR`
    - `MEX`
    - `MYS`
    - `NZL`
    """


class Individual(BaseModel):
    """Only present when user_type == "INDIVIDUAL".

    Information about the individual for which the account is being opened and KYC is being run.
    """

    address: Optional[IndividualAddress] = None
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB
    and KYC workflows.
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


class VerificationApplication(BaseModel):
    """Information about the most recent identity verification attempt"""

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

    ky_passed_at: Optional[datetime] = None
    """Timestamp of when the application passed the verification process.

    Only present if `status` is `ACCEPTED`
    """


class AccountHolderSimulateEnrollmentReviewResponse(BaseModel):
    token: Optional[str] = None
    """Globally unique identifier for the account holder."""

    account_token: Optional[str] = None
    """Globally unique identifier for the account."""

    beneficial_owner_individuals: Optional[List[BeneficialOwnerIndividual]] = None
    """Only present when user_type == "BUSINESS".

    You must submit a list of all direct and indirect individuals with 25% or more
    ownership in the company. A maximum of 4 beneficial owners can be submitted. If
    no individual owns 25% of the company you do not need to send beneficial owner
    information. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background on individuals that should be included.
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

    control_person: Optional[ControlPerson] = None
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
    """(Deprecated.

    Use control_person.email when user_type == "BUSINESS". Use
    individual.phone_number when user_type == "INDIVIDUAL".) Primary email of
    Account Holder.
    """

    exemption_type: Optional[Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"]] = None
    """The type of KYC exemption for a KYC-Exempt Account Holder.

    `null` if the account holder is not KYC-Exempt.
    """

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

    naics_code: Optional[str] = None
    """Only present when user_type == "BUSINESS".

    6-digit North American Industry Classification System (NAICS) code for the
    business.
    """

    nature_of_business: Optional[str] = None
    """Only present when user_type == "BUSINESS".

    User-submitted description of the business.
    """

    phone_number: Optional[str] = None
    """(Deprecated.

    Use control_person.phone_number when user_type == "BUSINESS". Use
    individual.phone_number when user_type == "INDIVIDUAL".) Primary phone of
    Account Holder, entered in E.164 format.
    """

    required_documents: Optional[List[RequiredDocument]] = None
    """Only present for "KYB_BASIC" and "KYC_ADVANCED" workflows.

    A list of documents required for the account holder to be approved.
    """

    status: Optional[Literal["ACCEPTED", "PENDING_DOCUMENT", "PENDING_RESUBMIT", "REJECTED"]] = None
    """(Deprecated.

    Use verification_application.status instead) KYC and KYB evaluation states.

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
    """(Deprecated.

    Use verification_application.status_reasons) Reason for the evaluation status.
    """

    user_type: Optional[Literal["BUSINESS", "INDIVIDUAL"]] = None
    """The type of Account Holder.

    If the type is "INDIVIDUAL", the "individual" attribute will be present.

    If the type is "BUSINESS" then the "business_entity", "control_person",
    "beneficial_owner_individuals", "naics_code", "nature_of_business", and
    "website_url" attributes will be present.
    """

    verification_application: Optional[VerificationApplication] = None
    """Information about the most recent identity verification attempt"""

    website_url: Optional[str] = None
    """Only present when user_type == "BUSINESS". Business's primary website."""
