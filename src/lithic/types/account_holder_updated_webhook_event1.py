# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .kyb_business_entity import KYBBusinessEntity

__all__ = [
    "AccountHolderUpdatedWebhookEvent",
    "KYBPayload",
    "KYBPayloadUpdateRequest",
    "KYBPayloadUpdateRequestBeneficialOwnerIndividual",
    "KYBPayloadUpdateRequestBeneficialOwnerIndividualAddress",
    "KYBPayloadUpdateRequestControlPerson",
    "KYBPayloadUpdateRequestControlPersonAddress",
    "KYCPayload",
    "KYCPayloadUpdateRequest",
    "KYCPayloadUpdateRequestIndividual",
    "KYCPayloadUpdateRequestIndividualAddress",
    "LegacyPayload",
]


class KYBPayloadUpdateRequestBeneficialOwnerIndividualAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

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


class KYBPayloadUpdateRequestBeneficialOwnerIndividual(BaseModel):
    address: Optional[KYBPayloadUpdateRequestBeneficialOwnerIndividualAddress] = None
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


class KYBPayloadUpdateRequestControlPersonAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

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


class KYBPayloadUpdateRequestControlPerson(BaseModel):
    """
    An individual with significant responsibility for managing the legal entity (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating Officer, Managing Member, General Partner, President, Vice President, or Treasurer). This can be an executive, or someone who will have program-wide access to the cards that Lithic will provide. In some cases, this individual could also be a beneficial owner listed above. See [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf) (Section II) for more background.
    """

    address: Optional[KYBPayloadUpdateRequestControlPersonAddress] = None
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


class KYBPayloadUpdateRequest(BaseModel):
    """Original request to update the account holder."""

    beneficial_owner_entities: Optional[List[KYBBusinessEntity]] = None
    """Deprecated."""

    beneficial_owner_individuals: Optional[List[KYBPayloadUpdateRequestBeneficialOwnerIndividual]] = None
    """
    You must submit a list of all direct and indirect individuals with 25% or more
    ownership in the company. A maximum of 4 beneficial owners can be submitted. If
    no individual owns 25% of the company you do not need to send beneficial owner
    information. See
    [FinCEN requirements](https://www.fincen.gov/sites/default/files/shared/CDD_Rev6.7_Sept_2017_Certificate.pdf)
    (Section I) for more background on individuals that should be included.
    """

    business_entity: Optional[KYBBusinessEntity] = None
    """
    Information for business for which the account is being opened and KYB is being
    run.
    """

    control_person: Optional[KYBPayloadUpdateRequestControlPerson] = None
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


class KYBPayload(BaseModel):
    """KYB payload for an updated account holder."""

    token: str
    """The token of the account_holder that was created."""

    update_request: KYBPayloadUpdateRequest
    """Original request to update the account holder."""

    event_type: Optional[Literal["account_holder.updated"]] = None
    """The type of event that occurred."""

    external_id: Optional[str] = None
    """
    A user provided id that can be used to link an account holder with an external
    system
    """

    nature_of_business: Optional[str] = None
    """
    Short description of the company's line of business (i.e., what does the company
    do?).
    """

    website_url: Optional[str] = None
    """Company website URL."""


class KYCPayloadUpdateRequestIndividualAddress(BaseModel):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

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


class KYCPayloadUpdateRequestIndividual(BaseModel):
    """
    Information on the individual for whom the account is being opened and KYC is being run.
    """

    address: Optional[KYCPayloadUpdateRequestIndividualAddress] = None
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


class KYCPayloadUpdateRequest(BaseModel):
    """Original request to update the account holder."""

    individual: Optional[KYCPayloadUpdateRequestIndividual] = None
    """
    Information on the individual for whom the account is being opened and KYC is
    being run.
    """


class KYCPayload(BaseModel):
    """KYC payload for an updated account holder."""

    token: str
    """The token of the account_holder that was created."""

    update_request: KYCPayloadUpdateRequest
    """Original request to update the account holder."""

    event_type: Optional[Literal["account_holder.updated"]] = None
    """The type of event that occurred."""

    external_id: Optional[str] = None
    """
    A user provided id that can be used to link an account holder with an external
    system
    """


class LegacyPayload(BaseModel):
    """Legacy payload for an updated account holder."""

    token: str
    """The token of the account_holder that was created."""

    business_account_token: Optional[str] = None
    """
    If applicable, represents the business account token associated with the
    account_holder.
    """

    created: Optional[datetime] = None
    """When the account_holder updated event was created"""

    email: Optional[str] = None
    """
    If updated, the newly updated email associated with the account_holder otherwise
    the existing email is provided.
    """

    event_type: Optional[Literal["account_holder.updated"]] = None
    """The type of event that occurred."""

    external_id: Optional[str] = None
    """If applicable, represents the external_id associated with the account_holder."""

    first_name: Optional[str] = None
    """If applicable, represents the account_holder's first name."""

    last_name: Optional[str] = None
    """If applicable, represents the account_holder's last name."""

    legal_business_name: Optional[str] = None
    """If applicable, represents the account_holder's business name."""

    phone_number: Optional[str] = None
    """
    If updated, the newly updated phone_number associated with the account_holder
    otherwise the existing phone_number is provided.
    """


AccountHolderUpdatedWebhookEvent: TypeAlias = Union[KYBPayload, KYCPayload, LegacyPayload]
