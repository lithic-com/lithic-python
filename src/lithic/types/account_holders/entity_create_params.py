# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..transaction_monitoring.entity_type import EntityType

__all__ = ["EntityCreateParams", "Address"]


class EntityCreateParams(TypedDict, total=False):
    address: Required[Address]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB
    and KYC workflows.
    """

    dob: Required[str]
    """Individual's date of birth, as an RFC 3339 date."""

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

    type: Required[EntityType]
    """The type of entity to create on the account holder"""


class Address(TypedDict, total=False):
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable. Only USA addresses are supported for the KYB and KYC workflows.
    """

    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """
    Valid country code, entered in uppercase ISO 3166-1 alpha-3 three-character
    format. Supported countries depend on the onboarding workflow used for the
    account holder.
    """

    address2: str
    """Unit or apartment number (if applicable)."""

    postal_code: Optional[str]
    """Valid postal code.

    For USA addresses, enter either a five-digit postal code or a nine-digit postal
    code (ZIP+4) using the format 12345-1234. Required for all countries except the
    following, which do not use postal codes: ABW, AGO, ARE, ATG, BDI, BEN, BFA,
    BHS, BLZ, BOL, BWA, CIV, CMR, COD, COG, COK, COM, DJI, DMA, ERI, FJI, GAB, GMB,
    GNQ, GRD, GUY, HKG, KIR, MAC, MLI, MRT, NIU, NRU, QAT, RWA, SLB, SLE, SSD, SUR,
    SXM, SYC, TGO, TKL, TLS, TON, TUV, UGA, VUT, YEM, ZWE
    """

    state: Optional[str]
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
