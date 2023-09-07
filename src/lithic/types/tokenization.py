# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tokenization"]


class Tokenization(BaseModel):
    token: str
    """
    A fixed-width 23-digit numeric identifier for the Transaction that may be set if
    the transaction originated from the Mastercard network. This number may be used
    for dispute tracking.
    """

    account_token: str
    """The account token associated with the card being tokenized."""

    card_token: str
    """The card token associated with the card being tokenized."""

    created_at: datetime
    """Date and time when the tokenization first occurred. UTC time zone."""

    status: Literal["APPROVED", "DECLINED", "REQUIRE_ADDITIONAL_AUTHENTICATION"]
    """The status of the tokenization request"""

    token_requestor_name: Literal["APPLE_PAY", "GOOGLE", "SAMSUNG_PAY"]
    """The entity that is requested the tokenization. Represents a Digital Wallet."""

    token_unique_reference: str
    """The network's unique reference for the tokenization."""

    updated_at: datetime
    """Latest date and time when the tokenization was updated. UTC time zone."""
