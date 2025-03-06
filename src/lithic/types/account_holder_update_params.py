# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .address_update_param import AddressUpdateParam

__all__ = [
    "AccountHolderUpdateParams",
    "KYBPatchRequest",
    "KYBPatchRequestBeneficialOwnerEntity",
    "KYBPatchRequestBeneficialOwnerIndividual",
    "KYBPatchRequestBusinessEntity",
    "KYBPatchRequestControlPerson",
    "KYCPatchRequest",
    "KYCPatchRequestIndividual",
    "PatchRequest",
]


class KYBPatchRequest(TypedDict, total=False):
    beneficial_owner_entities: Iterable[KYBPatchRequestBeneficialOwnerEntity]
    """List of all entities with >25% ownership in the company.

    If no entity or individual owns >25% of the company, and the largest shareholder
    is an entity, please identify them in this field. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)(Section
    I) for more background. If no business owner is an entity, pass in an empty
    list. However, either this parameter or `beneficial_owner_individuals` must be
    populated. on entities that should be included.
    """

    beneficial_owner_individuals: Iterable[KYBPatchRequestBeneficialOwnerIndividual]
    """List of all individuals with >25% ownership in the company.

    If no entity or individual owns >25% of the company, and the largest shareholder
    is an individual, please identify them in this field. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)(Section
    I) for more background on individuals that should be included. If no individual
    is an entity, pass in an empty list. However, either this parameter or
    `beneficial_owner_entities` must be populated.
    """

    business_entity: KYBPatchRequestBusinessEntity
    """
    Information for business for which the account is being opened and KYB is being
    run.
    """

    control_person: KYBPatchRequestControlPerson
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

    external_id: str
    """
    A user provided id that can be used to link an account holder with an external
    system
    """

    nature_of_business: str
    """
    Short description of the company's line of business (i.e., what does the company
    do?).
    """

    website_url: str
    """Company website URL."""


class KYBPatchRequestBeneficialOwnerEntity(TypedDict, total=False):
    entity_token: Required[str]
    """Globally unique identifier for an entity."""

    address: AddressUpdateParam
    """
    Business''s physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    dba_business_name: str
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    government_id: str
    """Government-issued identification number.

    US Federal Employer Identification Numbers (EIN) are currently supported,
    entered as full nine-digits, with or without hyphens.
    """

    legal_business_name: str
    """Legal (formal) business name."""

    parent_company: str
    """Parent company name (if applicable)."""

    phone_numbers: List[str]
    """
    One or more of the business's phone number(s), entered as a list in E.164
    format.
    """


class KYBPatchRequestBeneficialOwnerIndividual(TypedDict, total=False):
    entity_token: Required[str]
    """Globally unique identifier for an entity."""

    address: AddressUpdateParam
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
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


class KYBPatchRequestBusinessEntity(TypedDict, total=False):
    entity_token: Required[str]
    """Globally unique identifier for an entity."""

    address: AddressUpdateParam
    """
    Business''s physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    dba_business_name: str
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    government_id: str
    """Government-issued identification number.

    US Federal Employer Identification Numbers (EIN) are currently supported,
    entered as full nine-digits, with or without hyphens.
    """

    legal_business_name: str
    """Legal (formal) business name."""

    parent_company: str
    """Parent company name (if applicable)."""

    phone_numbers: List[str]
    """
    One or more of the business's phone number(s), entered as a list in E.164
    format.
    """


class KYBPatchRequestControlPerson(TypedDict, total=False):
    entity_token: Required[str]
    """Globally unique identifier for an entity."""

    address: AddressUpdateParam
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
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


class KYCPatchRequest(TypedDict, total=False):
    external_id: str
    """
    A user provided id that can be used to link an account holder with an external
    system
    """

    individual: KYCPatchRequestIndividual
    """
    Information on the individual for whom the account is being opened and KYC is
    being run.
    """


class KYCPatchRequestIndividual(TypedDict, total=False):
    entity_token: Required[str]
    """Globally unique identifier for an entity."""

    address: AddressUpdateParam
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: str
    """Individual's date of birth, as an RFC 3339 date."""

    email: str
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
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


class PatchRequest(TypedDict, total=False):
    address: AddressUpdateParam
    """Allowed for: KYC-Exempt, BYO-KYC, BYO-KYB."""

    business_account_token: str
    """Allowed for: KYC-Exempt, BYO-KYC.

    The token of the business account to which the account holder is associated.
    """

    email: str
    """Allowed for all Account Holders.

    Account holder's email address. The primary purpose of this field is for
    cardholder identification and verification during the digital wallet
    tokenization process.
    """

    first_name: str
    """Allowed for KYC-Exempt, BYO-KYC. Account holder's first name."""

    last_name: str
    """Allowed for KYC-Exempt, BYO-KYC. Account holder's last name."""

    legal_business_name: str
    """Allowed for BYO-KYB. Legal business name of the account holder."""

    phone_number: str
    """Allowed for all Account Holders.

    Account holder's phone number, entered in E.164 format. The primary purpose of
    this field is for cardholder identification and verification during the digital
    wallet tokenization process.
    """


AccountHolderUpdateParams: TypeAlias = Union[KYBPatchRequest, KYCPatchRequest, PatchRequest]
