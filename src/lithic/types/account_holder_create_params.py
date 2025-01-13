# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.address import Address

__all__ = [
    "AccountHolderCreateParams",
    "KYB",
    "KYBBeneficialOwnerEntity",
    "KYBBeneficialOwnerIndividual",
    "KYBBusinessEntity",
    "KYBControlPerson",
    "KYC",
    "KYCIndividual",
    "KYCExempt",
]


class KYB(TypedDict, total=False):
    beneficial_owner_entities: Required[Iterable[KYBBeneficialOwnerEntity]]
    """List of all entities with >25% ownership in the company.

    If no entity or individual owns >25% of the company, and the largest shareholder
    is an entity, please identify them in this field. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background. If no business owner is an entity, pass in an
    empty list. However, either this parameter or `beneficial_owner_individuals`
    must be populated. on entities that should be included.
    """

    beneficial_owner_individuals: Required[Iterable[KYBBeneficialOwnerIndividual]]
    """List of all direct and indirect individuals with >25% ownership in the company.

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
    An RFC 3339 timestamp indicating when the account holder accepted the applicable
    legal agreements (e.g., cardholder terms) as agreed upon during API customer's
    implementation with Lithic.
    """

    workflow: Required[Literal["KYB_BASIC", "KYB_BYO"]]
    """Specifies the type of KYB workflow to run."""

    external_id: str
    """
    A user provided id that can be used to link an account holder with an external
    system
    """

    kyb_passed_timestamp: str
    """
    An RFC 3339 timestamp indicating when precomputed KYC was completed on the
    business with a pass result.

    This field is required only if workflow type is `KYB_BYO`.
    """

    website_url: str
    """Company website URL."""


class KYBBeneficialOwnerEntity(TypedDict, total=False):
    address: Required[Address]
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


class KYBBeneficialOwnerIndividual(TypedDict, total=False):
    address: Required[Address]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an RFC 3339 date."""

    email: Required[str]
    """
    Individual's email address. If utilizing Lithic for chargeback processing, this
    customer email address may be used to communicate dispute status and resolution.
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

    phone_number: str
    """Individual's phone number, entered in E.164 format."""


class KYBBusinessEntity(TypedDict, total=False):
    address: Required[Address]
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


class KYBControlPerson(TypedDict, total=False):
    address: Required[Address]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an RFC 3339 date."""

    email: Required[str]
    """
    Individual's email address. If utilizing Lithic for chargeback processing, this
    customer email address may be used to communicate dispute status and resolution.
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

    phone_number: str
    """Individual's phone number, entered in E.164 format."""


class KYC(TypedDict, total=False):
    individual: Required[KYCIndividual]
    """
    Information on individual for whom the account is being opened and KYC is being
    run.
    """

    tos_timestamp: Required[str]
    """
    An RFC 3339 timestamp indicating when the account holder accepted the applicable
    legal agreements (e.g., cardholder terms) as agreed upon during API customer's
    implementation with Lithic.
    """

    workflow: Required[Literal["KYC_BASIC", "KYC_BYO"]]
    """Specifies the type of KYC workflow to run."""

    external_id: str
    """
    A user provided id that can be used to link an account holder with an external
    system
    """

    kyc_passed_timestamp: str
    """
    An RFC 3339 timestamp indicating when precomputed KYC was completed on the
    individual with a pass result.

    This field is required only if workflow type is `KYC_BYO`.
    """


class KYCIndividual(TypedDict, total=False):
    address: Required[Address]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an RFC 3339 date."""

    email: Required[str]
    """
    Individual's email address. If utilizing Lithic for chargeback processing, this
    customer email address may be used to communicate dispute status and resolution.
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


class KYCExempt(TypedDict, total=False):
    address: Required[Address]
    """
    KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    email: Required[str]
    """The KYC Exempt user's email"""

    first_name: Required[str]
    """The KYC Exempt user's first name"""

    kyc_exemption_type: Required[Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"]]
    """Specifies the type of KYC Exempt user"""

    last_name: Required[str]
    """The KYC Exempt user's last name"""

    phone_number: Required[str]
    """The KYC Exempt user's phone number, entered in E.164 format."""

    workflow: Required[Literal["KYC_EXEMPT"]]
    """Specifies the workflow type. This must be 'KYC_EXEMPT'"""

    business_account_token: str
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Pass the account_token of the enrolled business associated
    with the AUTHORIZED_USER in this field.
    """

    external_id: str
    """
    A user provided id that can be used to link an account holder with an external
    system
    """


AccountHolderCreateParams: TypeAlias = Union[KYB, KYC, KYCExempt]
