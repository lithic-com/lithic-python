# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["NetworkTotalListResponse", "Amounts"]


class Amounts(BaseModel):
    gross_settlement: int
    """Total settlement amount excluding interchange, in currency's smallest unit."""

    interchange_fees: int
    """Interchange amount, in currency's smallest unit."""

    net_settlement: int
    """
    `gross_settlement` net of `interchange_fees` and `visa_charges` (if applicable),
    in currency's smallest unit.
    """

    visa_charges: Optional[int] = None
    """Charges specific to Visa/Interlink, in currency's smallest unit."""


class NetworkTotalListResponse(BaseModel):
    token: str
    """Globally unique identifier."""

    amounts: Amounts

    created: datetime
    """RFC 3339 timestamp for when the record was created. UTC time zone."""

    currency: str
    """3-character alphabetic ISO 4217 code."""

    institution_id: str
    """The institution that activity occurred on.

    For Mastercard: ICA (Interbank Card Association). For Maestro: institution ID.
    For Visa: lowest level SRE (Settlement Reporting Entity).
    """

    network: Literal["VISA", "MASTERCARD", "MAESTRO", "INTERLINK"]
    """Card network where the transaction took place.

    VISA, MASTERCARD, MAESTRO, or INTERLINK.
    """

    report_date: date
    """Date that the network total record applies to. YYYY-MM-DD format."""

    settlement_institution_id: str
    """The institution responsible for settlement.

    For Mastercard: same as `institution_id`. For Maestro: billing ICA. For Visa:
    Funds Transfer SRE (FTSRE).
    """

    settlement_service: str
    """Settlement service."""

    updated: datetime
    """RFC 3339 timestamp for when the record was last updated. UTC time zone."""

    cycle: Optional[int] = None
    """The clearing cycle that the network total record applies to. Mastercard only."""
