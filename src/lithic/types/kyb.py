# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = ["KYB", "BeneficialOwnerEntity", "BeneficialOwnerIndividual", "BusinessEntity", "ControlPerson"]


class BeneficialOwnerEntity(BaseModel):
    address: shared.Address
    """
    Business's physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

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

    dba_business_name: Optional[str]
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    parent_company: Optional[str]
    """Parent company name (if applicable)."""


class BeneficialOwnerIndividual(BaseModel):
    address: shared.Address
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """
    Individual's email address. If utilizing Lithic for chargeback processing, this
    customer email address may be used to communicate dispute status and resolution.
    """

    first_name: str
    """Individual's first name, as it appears on government-issued identity documents."""

    government_id: str
    """
    Government-issued identification number (required for identity verification and
    compliance with banking regulations). Social Security Numbers (SSN) and
    Individual Taxpayer Identification Numbers (ITIN) are currently supported,
    entered as full nine-digits, with or without hyphens
    """

    last_name: str
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: str
    """Individual's phone number, entered in E.164 format."""


class BusinessEntity(BaseModel):
    address: shared.Address
    """
    Business's physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

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

    dba_business_name: Optional[str]
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    parent_company: Optional[str]
    """Parent company name (if applicable)."""


class ControlPerson(BaseModel):
    address: shared.Address
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """
    Individual's email address. If utilizing Lithic for chargeback processing, this
    customer email address may be used to communicate dispute status and resolution.
    """

    first_name: str
    """Individual's first name, as it appears on government-issued identity documents."""

    government_id: str
    """
    Government-issued identification number (required for identity verification and
    compliance with banking regulations). Social Security Numbers (SSN) and
    Individual Taxpayer Identification Numbers (ITIN) are currently supported,
    entered as full nine-digits, with or without hyphens
    """

    last_name: str
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: str
    """Individual's phone number, entered in E.164 format."""


class KYB(BaseModel):
    beneficial_owner_entities: List[BeneficialOwnerEntity]
    """List of all entities with >25% ownership in the company.

    If no entity or individual owns >25% of the company, and the largest shareholder
    is an entity, please identify them in this field. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background. If no business owner is an entity, pass in an
    empty list. However, either this parameter or `beneficial_owner_individuals`
    must be populated. on entities that should be included.
    """

    beneficial_owner_individuals: List[BeneficialOwnerIndividual]
    """List of all individuals with >25% ownership in the company.

    If no entity or individual owns >25% of the company, and the largest shareholder
    is an individual, please identify them in this field. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background on individuals that should be included. If no
    individual is an entity, pass in an empty list. However, either this parameter
    or `beneficial_owner_entities` must be populated.
    """

    business_entity: BusinessEntity
    """
    Information for business for which the account is being opened and KYB is being
    run.
    """

    control_person: ControlPerson
    """
    An individual with significant responsibility for managing the legal entity
    (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating
    Officer, Managing Member, General Partner, President, Vice President, or
    Treasurer). This can be an executive, or someone who will have program-wide
    access to the cards that Lithic will provide. In some cases, this individual
    could also be a beneficial owner listed above. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section II) for more background.
    """

    nature_of_business: str
    """
    Short description of the company's line of business (i.e., what does the company
    do?).
    """

    tos_timestamp: str
    """
    An RFC 3339 timestamp indicating when the account holder accepted the applicable
    legal agreements (e.g., cardholder terms) as agreed upon during API customer's
    implementation with Lithic.
    """

    website_url: str
    """Company website URL."""

    workflow: Literal["KYB_BASIC", "KYB_BYO"]
    """Specifies the type of KYB workflow to run."""

    kyb_passed_timestamp: Optional[str]
    """
    An RFC 3339 timestamp indicating when precomputed KYC was completed on the
    business with a pass result.

    This field is required only if workflow type is `KYB_BYO`.
    """
