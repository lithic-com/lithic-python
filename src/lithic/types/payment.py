# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .wire_party_details import WirePartyDetails

__all__ = [
    "Payment",
    "Event",
    "MethodAttributes",
    "MethodAttributesACHMethodAttributes",
    "MethodAttributesWireMethodAttributes",
    "RelatedAccountTokens",
]


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
        "ACH_ORIGINATION_REJECTED",
        "ACH_ORIGINATION_RELEASED",
        "ACH_ORIGINATION_REVIEWED",
        "ACH_ORIGINATION_SETTLED",
        "ACH_RECEIPT_PROCESSED",
        "ACH_RECEIPT_RELEASED",
        "ACH_RECEIPT_SETTLED",
        "ACH_RETURN_INITIATED",
        "ACH_RETURN_PROCESSED",
        "ACH_RETURN_REJECTED",
        "ACH_RETURN_SETTLED",
    ]
    """Event types:

    - `ACH_ORIGINATION_INITIATED` - ACH origination received and pending
      approval/release from an ACH hold.
    - `ACH_ORIGINATION_REVIEWED` - ACH origination has completed the review process.
    - `ACH_ORIGINATION_CANCELLED` - ACH origination has been cancelled.
    - `ACH_ORIGINATION_PROCESSED` - ACH origination has been processed and sent to
      the Federal Reserve.
    - `ACH_ORIGINATION_SETTLED` - ACH origination has settled.
    - `ACH_ORIGINATION_RELEASED` - ACH origination released from pending to
      available balance.
    - `ACH_ORIGINATION_REJECTED` - ACH origination was rejected and not sent to the
      Federal Reserve.
    - `ACH_RECEIPT_PROCESSED` - ACH receipt pending release from an ACH holder.
    - `ACH_RECEIPT_SETTLED` - ACH receipt funds have settled.
    - `ACH_RECEIPT_RELEASED` - ACH receipt released from pending to available
      balance.
    - `ACH_RETURN_INITIATED` - ACH initiated return for an ACH receipt.
    - `ACH_RETURN_PROCESSED` - ACH receipt returned by the Receiving Depository
      Financial Institution.
    - `ACH_RETURN_SETTLED` - ACH return settled by the Receiving Depository
      Financial Institution.
    - `ACH_RETURN_REJECTED` - ACH return was rejected by the Receiving Depository
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


class MethodAttributesACHMethodAttributes(BaseModel):
    sec_code: Literal["CCD", "PPD", "WEB", "TEL", "CIE", "CTX"]
    """SEC code for ACH transaction"""

    addenda: Optional[str] = None
    """Addenda information"""

    company_id: Optional[str] = None
    """Company ID for the ACH transaction"""

    receipt_routing_number: Optional[str] = None
    """Receipt routing number"""

    retries: Optional[int] = None
    """Number of retries attempted"""

    return_reason_code: Optional[str] = None
    """Return reason code if the transaction was returned"""

    trace_numbers: Optional[List[str]] = None
    """Trace numbers for the ACH transaction"""


class MethodAttributesWireMethodAttributes(BaseModel):
    wire_message_type: Optional[str] = None
    """Type of wire message"""

    wire_network: Literal["FEDWIRE", "SWIFT"]
    """Type of wire transfer"""

    creditor: Optional[WirePartyDetails] = None

    debtor: Optional[WirePartyDetails] = None

    message_id: Optional[str] = None
    """
    Point to point reference identifier, as assigned by the instructing party, used
    for tracking the message through the Fedwire system
    """

    remittance_information: Optional[str] = None
    """Payment details or invoice reference"""


MethodAttributes: TypeAlias = Union[MethodAttributesACHMethodAttributes, MethodAttributesWireMethodAttributes]


class RelatedAccountTokens(BaseModel):
    account_token: Optional[str] = None
    """Globally unique identifier for the account"""

    business_account_token: Optional[str] = None
    """Globally unique identifier for the business account"""


class Payment(BaseModel):
    token: str
    """Unique identifier for the transaction"""

    category: Literal[
        "ACH",
        "BALANCE_OR_FUNDING",
        "FEE",
        "REWARD",
        "ADJUSTMENT",
        "DERECOGNITION",
        "DISPUTE",
        "CARD",
        "EXTERNAL_ACH",
        "EXTERNAL_CHECK",
        "EXTERNAL_TRANSFER",
        "EXTERNAL_WIRE",
        "MANAGEMENT_ADJUSTMENT",
        "MANAGEMENT_DISPUTE",
        "MANAGEMENT_FEE",
        "MANAGEMENT_REWARD",
        "MANAGEMENT_DISBURSEMENT",
        "PROGRAM_FUNDING",
    ]
    """Transaction category"""

    created: datetime
    """ISO 8601 timestamp of when the transaction was created"""

    descriptor: str
    """Transaction descriptor"""

    direction: Literal["CREDIT", "DEBIT"]
    """Transfer direction"""

    events: List[Event]
    """List of transaction events"""

    family: Literal["PAYMENT"]
    """PAYMENT - Payment Transaction"""

    financial_account_token: str
    """Financial account token"""

    method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY", "WIRE"]
    """Transfer method"""

    method_attributes: MethodAttributes
    """Method-specific attributes"""

    pending_amount: int
    """Pending amount in cents"""

    related_account_tokens: RelatedAccountTokens
    """Related account tokens for the transaction"""

    result: Literal["APPROVED", "DECLINED"]
    """Transaction result"""

    settled_amount: int
    """Settled amount in cents"""

    source: Literal["LITHIC", "EXTERNAL", "CUSTOMER"]
    """Transaction source"""

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]
    """The status of the transaction"""

    updated: datetime
    """ISO 8601 timestamp of when the transaction was last updated"""

    currency: Optional[str] = None
    """Currency of the transaction in ISO 4217 format"""

    expected_release_date: Optional[date] = None
    """Expected release date for the transaction"""

    external_bank_account_token: Optional[str] = None
    """External bank account token"""

    type: Optional[
        Literal[
            "ORIGINATION_CREDIT",
            "ORIGINATION_DEBIT",
            "RECEIPT_CREDIT",
            "RECEIPT_DEBIT",
            "WIRE_INBOUND_PAYMENT",
            "WIRE_INBOUND_ADMIN",
            "WIRE_OUTBOUND_PAYMENT",
            "WIRE_OUTBOUND_ADMIN",
        ]
    ] = None

    user_defined_id: Optional[str] = None
    """User-defined identifier"""
