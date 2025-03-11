# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CardProgram"]


class CardProgram(BaseModel):
    token: str
    """Globally unique identifier."""

    created: datetime
    """Timestamp of when the card program was created."""

    name: str
    """The name of the card program."""

    pan_range_end: str
    """The first digits of the card number that this card program ends with."""

    pan_range_start: str
    """The first digits of the card number that this card program starts with."""

    cardholder_currency: Optional[str] = None
    """3-character alphabetic ISO 4217 code for the currency of the cardholder."""

    settlement_currencies: Optional[List[str]] = None
    """
    List of 3-character alphabetic ISO 4217 codes for the currencies that the card
    program supports for settlement.
    """
