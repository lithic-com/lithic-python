# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["CaseTransaction"]


class CaseTransaction(BaseModel):
    """A single transaction associated with a case"""

    token: str
    """Globally unique identifier for the transaction"""

    account_token: str
    """Token of the account the transaction belongs to"""

    added_at: datetime
    """Date and time at which the transaction was added to the case"""

    card_token: str
    """Token of the card the transaction was made on"""

    transaction_created_at: datetime
    """Date and time at which the transaction was created"""
