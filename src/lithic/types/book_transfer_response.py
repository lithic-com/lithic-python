# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BookTransferResponse", "Event"]


class Event(BaseModel):
    token: str
    """Globally unique identifier."""

    amount: int
    """
    Amount of the financial event that has been settled in the currency's smallest
    unit (e.g., cents).
    """

    created: datetime
    """Date and time when the financial event occurred. UTC time zone."""

    detailed_results: List[Literal["APPROVED", "FUNDS_INSUFFICIENT"]]
    """Detailed Results"""

    memo: str
    """Memo for the transfer."""

    result: Literal["APPROVED", "DECLINED"]
    """
    APPROVED financial events were successful while DECLINED financial events were
    declined by user, Lithic, or the network.
    """

    subtype: str
    """The program specific subtype code for the specified category/type."""

    type: str
    """Type of the book transfer"""


class BookTransferResponse(BaseModel):
    token: str
    """Customer-provided token that will serve as an idempotency token.

    This token will become the transaction token.
    """

    category: Literal["ADJUSTMENT", "BALANCE_OR_FUNDING", "DERECOGNITION", "DISPUTE", "FEE", "REWARD", "TRANSFER"]
    """Category of the book transfer"""

    created: datetime
    """Date and time when the transfer occurred. UTC time zone."""

    currency: str
    """
    3-character alphabetic ISO 4217 code for the settling currency of the
    transaction.
    """

    events: List[Event]
    """A list of all financial events that have modified this transfer."""

    from_financial_account_token: str
    """
    Globally unique identifier for the financial account or card that will send the
    funds. Accepted type dependent on the program's use case.
    """

    pending_amount: int
    """
    Pending amount of the transaction in the currency's smallest unit (e.g., cents),
    including any acquirer fees. The value of this field will go to zero over time
    once the financial transaction is settled.
    """

    result: Literal["APPROVED", "DECLINED"]
    """
    APPROVED transactions were successful while DECLINED transactions were declined
    by user, Lithic, or the network.
    """

    settled_amount: int
    """
    Amount of the transaction that has been settled in the currency's smallest unit
    (e.g., cents).
    """

    status: Literal["DECLINED", "REVERSED", "SETTLED"]
    """Status types: \\** `DECLINED` - The transfer was declined.

    - `REVERSED` - The transfer was reversed \\** `SETTLED` - The transfer is
      completed.
    """

    to_financial_account_token: object
    """
    Globally unique identifier for the financial account or card that will receive
    the funds. Accepted type dependent on the program's use case.
    """

    updated: datetime
    """Date and time when the financial transaction was last updated. UTC time zone."""
