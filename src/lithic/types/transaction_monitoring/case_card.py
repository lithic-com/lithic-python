# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CaseCard"]


class CaseCard(BaseModel):
    """
    Summary of a card's involvement in a case, aggregated across the case's transactions
    """

    account_token: str
    """Token of the account the card belongs to"""

    card_token: str
    """Token of the card"""

    transaction_count: int
    """Number of the card's transactions associated with the case"""
