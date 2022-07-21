# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "KYBBusinessEntityAddress",
    "KYBBusinessEntity",
    "KYBBeneficialOwnerEntitiesAddress",
    "KYBBeneficialOwnerEntities",
    "KYBBeneficialOwnerIndividualsAddress",
    "KYBBeneficialOwnerIndividuals",
    "KYBControlPersonAddress",
    "KYBControlPerson",
    "KYB",
    "KYCIndividualAddress",
    "KYCIndividual",
    "KYC",
    "AccountHolderCreateParams",
]


class KYBBusinessEntityAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: Required[str]
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: str
    """Unit or apartment number (if applicable)."""


class KYBBusinessEntity(TypedDict, total=False):
    address: Required[KYBBusinessEntityAddress]
    """
    Business's physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    government_id: Required[str]
    """Government-issued identification number.

    US Federal Employer Identification Numbers (EIN) are currently supported,
    entered as full nine-digits, with or without hyphens.
    """

    legal_business_name: Required[str]
    """Legal (formal) business name."""

    phone_numbers: Required[List[str]]
    """
    One or more of the business's phone number(s), entered as a list in E.164
    format.
    """

    dba_business_name: str
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    parent_company: str
    """Parent company name (if applicable)."""


class KYBBeneficialOwnerEntitiesAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: Required[str]
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: str
    """Unit or apartment number (if applicable)."""


class KYBBeneficialOwnerEntities(TypedDict, total=False):
    address: Required[KYBBeneficialOwnerEntitiesAddress]
    """
    Business's physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    government_id: Required[str]
    """Government-issued identification number.

    US Federal Employer Identification Numbers (EIN) are currently supported,
    entered as full nine-digits, with or without hyphens.
    """

    legal_business_name: Required[str]
    """Legal (formal) business name."""

    phone_numbers: Required[List[str]]
    """
    One or more of the business's phone number(s), entered as a list in E.164
    format.
    """

    dba_business_name: str
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    parent_company: str
    """Parent company name (if applicable)."""


class KYBBeneficialOwnerIndividualsAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: Required[str]
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: str
    """Unit or apartment number (if applicable)."""


class KYBBeneficialOwnerIndividuals(TypedDict, total=False):
    address: Required[KYBBeneficialOwnerIndividualsAddress]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an ISO 8601 date."""

    email: Required[str]
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Required[str]
    """Individual's first name, as it appears on government-issued identity documents."""

    government_id: Required[str]
    """
    Government-issued identification number (required for identity verification and
    compliance with banking regulations). Social Security Numbers (SSN) and
    Individual Taxpayer Identification Numbers (ITIN) are currently supported,
    entered as full nine-digits, with or without hyphens
    """

    last_name: Required[str]
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Required[str]
    """Individual's phone number, entered in E.164 format."""


class KYBControlPersonAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: Required[str]
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: str
    """Unit or apartment number (if applicable)."""


class KYBControlPerson(TypedDict, total=False):
    address: Required[KYBControlPersonAddress]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an ISO 8601 date."""

    email: Required[str]
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Required[str]
    """Individual's first name, as it appears on government-issued identity documents."""

    government_id: Required[str]
    """
    Government-issued identification number (required for identity verification and
    compliance with banking regulations). Social Security Numbers (SSN) and
    Individual Taxpayer Identification Numbers (ITIN) are currently supported,
    entered as full nine-digits, with or without hyphens
    """

    last_name: Required[str]
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Required[str]
    """Individual's phone number, entered in E.164 format."""


class KYB(TypedDict, total=False):
    beneficial_owner_entities: Required[List[KYBBeneficialOwnerEntities]]
    """List of all entities with >25% ownership in the company.

    If no entity or individual owns >25% of the company, and the largest shareholder
    is an entity, please identify them in this field. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background. If no business owner is an entity, pass in an
    empty list. However, either this parameter or `beneficial_owner_individuals`
    must be populated. on entities that should be included.
    """

    beneficial_owner_individuals: Required[List[KYBBeneficialOwnerIndividuals]]
    """List of all individuals with >25% ownership in the company.

    If no entity or individual owns >25% of the company, and the largest shareholder
    is an individual, please identify them in this field. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background on individuals that should be included. If no
    individual is an entity, pass in an empty list. However, either this parameter
    or `beneficial_owner_entities` must be populated.
    """

    business_entity: Required[KYBBusinessEntity]
    """
    Information for business for which the account is being opened and KYB is being
    run.
    """

    control_person: Required[KYBControlPerson]
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

    nature_of_business: Required[str]
    """
    Short description of the company's line of business (i.e., what does the company
    do?).
    """

    tos_timestamp: Required[str]
    """
    An ISO 8601 timestamp indicating when the account holder accepted the applicable
    legal agreements (e.g., cardholder terms) as agreed upon during API customer's
    implementation with Lithic.
    """

    website_url: Required[str]
    """Company website URL."""

    workflow: Required[Literal["KYB_BASIC", "KYB_BYO"]]
    """Specifies the type of KYB workflow to run."""

    kyb_passed_timestamp: str
    """
    An ISO 8601 timestamp indicating when precomputed KYC was completed on the
    business with a pass result.

    This field is required only if workflow type is `KYB_BYO`.
    """


class KYCIndividualAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: Required[str]
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: str
    """Unit or apartment number (if applicable)."""


class KYCIndividual(TypedDict, total=False):
    address: Required[KYCIndividualAddress]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an ISO 8601 date."""

    email: Required[str]
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Required[str]
    """Individual's first name, as it appears on government-issued identity documents."""

    government_id: Required[str]
    """
    Government-issued identification number (required for identity verification and
    compliance with banking regulations). Social Security Numbers (SSN) and
    Individual Taxpayer Identification Numbers (ITIN) are currently supported,
    entered as full nine-digits, with or without hyphens
    """

    last_name: Required[str]
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Required[str]
    """Individual's phone number, entered in E.164 format."""


class KYC(TypedDict, total=False):
    individual: Required[KYCIndividual]
    """
    Information on individual for whom the account is being opened and KYC is being
    run.
    """

    tos_timestamp: Required[str]
    """
    An ISO 8601 timestamp indicating when the account holder accepted the applicable
    legal agreements (e.g., cardholder terms) as agreed upon during API customer's
    implementation with Lithic.
    """

    workflow: Required[Literal["KYC_ADVANCED", "KYC_BASIC", "KYC_BYO"]]
    """Specifies the type of KYC workflow to run."""

    kyc_passed_timestamp: str
    """
    An ISO 8601 timestamp indicating when precomputed KYC was completed on the
    individual with a pass result.

    This field is required only if workflow type is `KYC_BYO`.
    """


AccountHolderCreateParams = Union[KYB, KYC]
