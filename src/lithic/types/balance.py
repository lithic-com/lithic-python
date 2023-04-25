# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Balance"]


class Balance(BaseModel):
    available_amount: int
    """Funds available for spend in the currency's smallest unit (e.g., cents for USD)"""

    created: datetime
    """Date and time for when the balance was first created."""

    currency: str
    """3-digit alphabetic ISO 4217 code for the local currency of the balance."""

    last_transaction_event_token: str
    """
    Globally unique identifier for the last financial transaction event that
    impacted this balance.
    """

    last_transaction_token: str
    """
    Globally unique identifier for the last financial transaction that impacted this
    balance.
    """

    pending_amount: int
    """Funds not available for spend due to card authorizations or pending ACH release.

    Shown in the currency's smallest unit (e.g., cents for USD).
    """

    token: str
    """Globally unique identifier for the financial account that holds this balance."""

    total_amount: int
    """
    The sum of available and pending balance in the currency's smallest unit (e.g.,
    cents for USD).
    """

    type: Literal["ISSUING", "RESERVE"]
    """Type of financial account."""

    updated: datetime
    """Date and time for when the balance was last updated."""
