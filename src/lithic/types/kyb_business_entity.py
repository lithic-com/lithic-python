# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["KYBBusinessEntity", "Address"]


class Address(BaseModel):
    """
    Business''s physical address - PO boxes, UPS drops, and FedEx drops are not acceptable; APO/FPO are acceptable.
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


class KYBBusinessEntity(BaseModel):
    address: Address
    """
    Business''s physical address - PO boxes, UPS drops, and FedEx drops are not
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

    dba_business_name: Optional[str] = None
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    parent_company: Optional[str] = None
    """Parent company name (if applicable)."""
