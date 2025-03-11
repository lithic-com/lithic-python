# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Payment", "Event", "MethodAttributes"]


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

    result: Literal["APPROVED", "DECLINED"]
    """
    APPROVED financial events were successful while DECLINED financial events were
    declined by user, Lithic, or the network.
    """

    type: Literal[
        "ACH_ORIGINATION_CANCELLED",
        "ACH_ORIGINATION_INITIATED",
        "ACH_ORIGINATION_PROCESSED",
        "ACH_ORIGINATION_SETTLED",
        "ACH_ORIGINATION_RELEASED",
        "ACH_ORIGINATION_REVIEWED",
        "ACH_RECEIPT_PROCESSED",
        "ACH_RECEIPT_SETTLED",
        "ACH_RETURN_INITIATED",
        "ACH_RETURN_PROCESSED",
        "ACH_RETURN_SETTLED",
    ]
    """Event types:

    - `ACH_ORIGINATION_INITIATED` - ACH origination received and pending
      approval/release from an ACH hold.
    - `ACH_ORIGINATION_REVIEWED` - ACH origination has completed the review process.
    - `ACH_ORIGINATION_CANCELLED` - ACH origination has been cancelled.
    - `ACH_ORIGINATION_PROCESSED` - ACH origination has been processed and sent to
      the fed.
    - `ACH_ORIGINATION_SETTLED` - ACH origination has settled.
    - `ACH_ORIGINATION_RELEASED` - ACH origination released from pending to
      available balance.
    - `ACH_RETURN_PROCESSED` - ACH origination returned by the Receiving Depository
      Financial Institution.
    - `ACH_RECEIPT_PROCESSED` - ACH receipt pending release from an ACH holder.
    - `ACH_RETURN_INITIATED` - ACH initiated return for a ACH receipt.
    - `ACH_RECEIPT_SETTLED` - ACH receipt funds have settled.
    - `ACH_RECEIPT_RELEASED` - ACH receipt released from pending to available
      balance.
    - `ACH_RETURN_SETTLED` - ACH receipt return settled by the Receiving Depository
      Financial Institution.
    """

    detailed_results: Optional[
        List[
            Literal[
                "APPROVED",
                "FUNDS_INSUFFICIENT",
                "ACCOUNT_INVALID",
                "PROGRAM_TRANSACTION_LIMIT_EXCEEDED",
                "PROGRAM_DAILY_LIMIT_EXCEEDED",
                "PROGRAM_MONTHLY_LIMIT_EXCEEDED",
            ]
        ]
    ] = None
    """More detailed reasons for the event"""


class MethodAttributes(BaseModel):
    company_id: Optional[str] = None

    receipt_routing_number: Optional[str] = None

    retries: Optional[int] = None

    return_reason_code: Optional[str] = None

    sec_code: Literal["CCD", "PPD", "WEB"]

    trace_numbers: List[Optional[str]]


class Payment(BaseModel):
    token: str
    """Globally unique identifier."""

    category: Literal["ACH"]
    """Payment category"""

    created: datetime
    """Date and time when the payment first occurred. UTC time zone."""

    currency: str
    """3-character alphabetic ISO 4217 code for the settling currency of the payment."""

    descriptor: str
    """
    A string that provides a description of the payment; may be useful to display to
    users.
    """

    direction: Literal["CREDIT", "DEBIT"]

    events: List[Event]
    """A list of all payment events that have modified this payment."""

    external_bank_account_token: Optional[str] = None

    financial_account_token: str

    method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"]

    method_attributes: MethodAttributes

    pending_amount: int
    """
    Pending amount of the payment in the currency's smallest unit (e.g., cents). The
    value of this field will go to zero over time once the payment is settled.
    """

    result: Literal["APPROVED", "DECLINED"]
    """
    APPROVED payments were successful while DECLINED payments were declined by
    Lithic or returned.
    """

    settled_amount: int
    """
    Amount of the payment that has been settled in the currency's smallest unit
    (e.g., cents).
    """

    source: Literal["CUSTOMER", "LITHIC"]

    status: Literal["DECLINED", "PENDING", "RETURNED", "SETTLED"]
    """Status types:

    - `DECLINED` - The payment was declined.
    - `PENDING` - The payment is being processed and has yet to settle or release
      (origination debit).
    - `RETURNED` - The payment has been returned.
    - `SETTLED` - The payment is completed.
    """

    updated: datetime
    """Date and time when the financial transaction was last updated. UTC time zone."""

    user_defined_id: Optional[str] = None
