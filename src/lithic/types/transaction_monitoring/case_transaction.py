# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["CaseTransaction", "CardCaseTransaction", "PaymentCaseTransaction"]


class CardCaseTransaction(BaseModel):
    """A card transaction associated with a case"""

    token: str
    """Globally unique identifier for the card transaction"""

    account_token: str
    """Token of the account the transaction belongs to"""

    added_at: datetime
    """Date and time at which the transaction was added to the case"""

    card_token: str
    """Token of the card the transaction was made on"""

    category: Literal["CARD"]

    transaction_created_at: datetime
    """Date and time at which the transaction was created"""


class PaymentCaseTransaction(BaseModel):
    """A payment (ACH) transaction associated with a case"""

    token: str
    """Globally unique identifier for the payment transaction"""

    added_at: datetime
    """Date and time at which the transaction was added to the case"""

    category: Literal["PAYMENT"]

    financial_account_token: str
    """Token of the financial account the payment belongs to"""

    transaction_created_at: datetime
    """Date and time at which the transaction was created"""

    account_token: Optional[str] = None
    """Token of the account the payment belongs to, if applicable"""


CaseTransaction: TypeAlias = Union[CardCaseTransaction, PaymentCaseTransaction]
