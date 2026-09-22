# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..transaction_monitoring.entity_type import EntityType

__all__ = ["AccountHolderEntity", "Address"]


class Address(BaseModel):
    """Individual's current address"""

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


class AccountHolderEntity(BaseModel):
    """Information about an entity associated with an account holder"""

    token: str
    """Globally unique identifier for the entity"""

    account_holder_token: str
    """Globally unique identifier for the account holder"""

    address: Address
    """Individual's current address"""

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date"""

    email: Optional[str] = None
    """Individual's email address"""

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents"""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents"""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format"""

    status: Literal["ACCEPTED", "INACTIVE", "PENDING_REVIEW", "REJECTED"]
    """The status of the entity"""

    type: EntityType
    """The type of entity"""
