# File generated from our OpenAPI spec by Stainless.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["AggregateBalanceListResponse"]


class AggregateBalanceListResponse(BaseModel):
    available_amount: int
    """Funds available for spend in the currency's smallest unit (e.g., cents for USD)"""

    created: datetime
    """Date and time for when the balance was first created."""

    currency: str
    """3-digit alphabetic ISO 4217 code for the local currency of the balance."""

    last_card_token: str
    """
    Globally unique identifier for the card that had its balance updated most
    recently
    """

    last_transaction_event_token: str
    """
    Globally unique identifier for the last transaction event that impacted this
    balance
    """

    last_transaction_token: str
    """Globally unique identifier for the last transaction that impacted this balance"""

    pending_amount: int
    """Funds not available for spend due to card authorizations or pending ACH release.

    Shown in the currency's smallest unit (e.g., cents for USD)
    """

    total_amount: int
    """
    The sum of available and pending balance in the currency's smallest unit (e.g.,
    cents for USD)
    """

    updated: datetime
    """Date and time for when the balance was last updated."""
