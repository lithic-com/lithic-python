# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .transaction import Transaction
from .external_payment import ExternalPayment
from .external_resource import ExternalResource
from .wire_party_details import WirePartyDetails
from .management_operation_transaction import ManagementOperationTransaction

__all__ = [
    "AccountActivityListResponse",
    "FinancialTransaction",
    "FinancialTransactionEvent",
    "BookTransferTransaction",
    "BookTransferTransactionEvent",
    "BookTransferTransactionTransactionSeries",
    "CardTransaction",
    "PaymentTransaction",
    "PaymentTransactionEvent",
    "PaymentTransactionMethodAttributes",
    "PaymentTransactionMethodAttributesACHMethodAttributes",
    "PaymentTransactionMethodAttributesWireMethodAttributes",
    "PaymentTransactionRelatedAccountTokens",
]


class FinancialTransactionEvent(BaseModel):
    token: Optional[str] = None
    """Globally unique identifier."""

    amount: Optional[int] = None
    """
    Amount of the financial event that has been settled in the currency's smallest
    unit (e.g., cents).
    """

    created: Optional[datetime] = None
    """Date and time when the financial event occurred. UTC time zone."""

    result: Optional[Literal["APPROVED", "DECLINED"]] = None
    """
    APPROVED financial events were successful while DECLINED financial events were
    declined by user, Lithic, or the network.
    """

    type: Optional[
        Literal[
            "ACH_ORIGINATION_CANCELLED",
            "ACH_ORIGINATION_INITIATED",
            "ACH_ORIGINATION_PROCESSED",
            "ACH_ORIGINATION_RELEASED",
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_PROCESSED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_SETTLED",
            "AUTHORIZATION",
            "AUTHORIZATION_ADVICE",
            "AUTHORIZATION_EXPIRY",
            "AUTHORIZATION_REVERSAL",
            "BALANCE_INQUIRY",
            "BILLING_ERROR",
            "BILLING_ERROR_REVERSAL",
            "CARD_TO_CARD",
            "CASH_BACK",
            "CASH_BACK_REVERSAL",
            "CLEARING",
            "COLLECTION",
            "CORRECTION_CREDIT",
            "CORRECTION_DEBIT",
            "CREDIT_AUTHORIZATION",
            "CREDIT_AUTHORIZATION_ADVICE",
            "CURRENCY_CONVERSION",
            "CURRENCY_CONVERSION_REVERSAL",
            "DISPUTE_WON",
            "EXTERNAL_ACH_CANCELED",
            "EXTERNAL_ACH_INITIATED",
            "EXTERNAL_ACH_RELEASED",
            "EXTERNAL_ACH_REVERSED",
            "EXTERNAL_ACH_SETTLED",
            "EXTERNAL_CHECK_CANCELED",
            "EXTERNAL_CHECK_INITIATED",
            "EXTERNAL_CHECK_RELEASED",
            "EXTERNAL_CHECK_REVERSED",
            "EXTERNAL_CHECK_SETTLED",
            "EXTERNAL_TRANSFER_CANCELED",
            "EXTERNAL_TRANSFER_INITIATED",
            "EXTERNAL_TRANSFER_RELEASED",
            "EXTERNAL_TRANSFER_REVERSED",
            "EXTERNAL_TRANSFER_SETTLED",
            "EXTERNAL_WIRE_CANCELED",
            "EXTERNAL_WIRE_INITIATED",
            "EXTERNAL_WIRE_RELEASED",
            "EXTERNAL_WIRE_REVERSED",
            "EXTERNAL_WIRE_SETTLED",
            "FINANCIAL_AUTHORIZATION",
            "FINANCIAL_CREDIT_AUTHORIZATION",
            "INTEREST",
            "INTEREST_REVERSAL",
            "INTERNAL_ADJUSTMENT",
            "LATE_PAYMENT",
            "LATE_PAYMENT_REVERSAL",
            "LOSS_WRITE_OFF",
            "PROVISIONAL_CREDIT",
            "PROVISIONAL_CREDIT_REVERSAL",
            "SERVICE",
            "RETURN",
            "RETURN_REVERSAL",
            "TRANSFER",
            "TRANSFER_INSUFFICIENT_FUNDS",
            "RETURNED_PAYMENT",
            "RETURNED_PAYMENT_REVERSAL",
            "LITHIC_NETWORK_PAYMENT",
        ]
    ] = None


class FinancialTransaction(BaseModel):
    token: str
    """Unique identifier for the transaction"""

    category: Literal[
        "ACH",
        "BALANCE_OR_FUNDING",
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

    currency: str
    """Currency of the transaction, represented in ISO 4217 format"""

    descriptor: str
    """Transaction descriptor"""

    events: List[FinancialTransactionEvent]
    """List of transaction events"""

    family: Literal["CARD", "PAYMENT", "TRANSFER", "INTERNAL", "EXTERNAL_PAYMENT", "MANAGEMENT_OPERATION"]

    financial_account_token: str
    """Financial account token associated with the transaction"""

    pending_amount: int
    """Pending amount in cents"""

    result: Literal["APPROVED", "DECLINED"]
    """Transaction result"""

    settled_amount: int
    """Settled amount in cents"""

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]
    """The status of the transaction"""

    updated: datetime
    """ISO 8601 timestamp of when the transaction was last updated"""


class BookTransferTransactionEvent(BaseModel):
    token: str
    """Globally unique identifier."""

    amount: int
    """
    Amount of the financial event that has been settled in the currency's smallest
    unit (e.g., cents).
    """

    created: datetime
    """Date and time when the financial event occurred. UTC time zone."""

    detailed_results: Literal["APPROVED", "FUNDS_INSUFFICIENT"]

    memo: str
    """Memo for the transfer."""

    result: Literal["APPROVED", "DECLINED"]
    """
    APPROVED financial events were successful while DECLINED financial events were
    declined by user, Lithic, or the network.
    """

    subtype: str
    """The program specific subtype code for the specified category/type."""

    type: Literal[
        "ATM_WITHDRAWAL",
        "ATM_DECLINE",
        "INTERNATIONAL_ATM_WITHDRAWAL",
        "INACTIVITY",
        "STATEMENT",
        "MONTHLY",
        "QUARTERLY",
        "ANNUAL",
        "CUSTOMER_SERVICE",
        "ACCOUNT_MAINTENANCE",
        "ACCOUNT_ACTIVATION",
        "ACCOUNT_CLOSURE",
        "CARD_REPLACEMENT",
        "CARD_DELIVERY",
        "CARD_CREATE",
        "CURRENCY_CONVERSION",
        "INTEREST",
        "LATE_PAYMENT",
        "BILL_PAYMENT",
        "CASH_BACK",
        "ACCOUNT_TO_ACCOUNT",
        "CARD_TO_CARD",
        "DISBURSE",
        "BILLING_ERROR",
        "LOSS_WRITE_OFF",
        "EXPIRED_CARD",
        "EARLY_DERECOGNITION",
        "ESCHEATMENT",
        "INACTIVITY_FEE_DOWN",
        "PROVISIONAL_CREDIT",
        "DISPUTE_WON",
        "SERVICE",
        "TRANSFER",
        "COLLECTION",
    ]
    """Type of the book transfer"""


class BookTransferTransactionTransactionSeries(BaseModel):
    related_transaction_event_token: Optional[str] = None

    related_transaction_token: Optional[str] = None

    type: str


class BookTransferTransaction(BaseModel):
    token: str
    """Unique identifier for the transaction"""

    category: Literal[
        "ACH",
        "BALANCE_OR_FUNDING",
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

    created: datetime
    """ISO 8601 timestamp of when the transaction was created"""

    currency: str
    """Currency of the transaction in ISO 4217 format"""

    events: List[BookTransferTransactionEvent]
    """List of events associated with this book transfer"""

    family: Literal["CARD", "PAYMENT", "TRANSFER", "INTERNAL", "EXTERNAL_PAYMENT", "MANAGEMENT_OPERATION"]

    from_financial_account_token: str
    """Source account token"""

    pending_amount: int
    """The pending amount of the transaction in cents"""

    result: Literal["APPROVED", "DECLINED"]

    settled_amount: int
    """The settled amount of the transaction in cents"""

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]
    """The status of the transaction"""

    to_financial_account_token: str
    """Destination account token"""

    updated: datetime
    """ISO 8601 timestamp of when the transaction was last updated"""

    external_id: Optional[str] = None
    """External identifier for the transaction"""

    external_resource: Optional[ExternalResource] = None
    """External resource associated with the management operation"""

    transaction_series: Optional[BookTransferTransactionTransactionSeries] = None


class CardTransaction(Transaction):
    token: str  # type: ignore
    """Unique identifier for the transaction"""

    created: datetime  # type: ignore
    """ISO 8601 timestamp of when the transaction was created"""

    family: Literal["CARD", "PAYMENT", "TRANSFER", "INTERNAL", "EXTERNAL_PAYMENT", "MANAGEMENT_OPERATION"]

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]  # type: ignore
    """The status of the transaction"""

    updated: datetime  # type: ignore
    """ISO 8601 timestamp of when the transaction was last updated"""


class PaymentTransactionEvent(BaseModel):
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
      the Federal Reserve.
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


class PaymentTransactionMethodAttributesACHMethodAttributes(BaseModel):
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


class PaymentTransactionMethodAttributesWireMethodAttributes(BaseModel):
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

    wire_message_type: Optional[str] = None
    """Type of wire message"""


PaymentTransactionMethodAttributes: TypeAlias = Union[
    PaymentTransactionMethodAttributesACHMethodAttributes, PaymentTransactionMethodAttributesWireMethodAttributes
]


class PaymentTransactionRelatedAccountTokens(BaseModel):
    account_token: Optional[str] = None
    """Globally unique identifier for the account"""

    business_account_token: Optional[str] = None
    """Globally unique identifier for the business account"""


class PaymentTransaction(BaseModel):
    token: str
    """Unique identifier for the transaction"""

    category: Literal[
        "ACH",
        "BALANCE_OR_FUNDING",
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

    events: List[PaymentTransactionEvent]
    """List of transaction events"""

    family: Literal["CARD", "PAYMENT", "TRANSFER", "INTERNAL", "EXTERNAL_PAYMENT", "MANAGEMENT_OPERATION"]

    financial_account_token: str
    """Financial account token"""

    method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY", "WIRE"]
    """Transfer method"""

    method_attributes: PaymentTransactionMethodAttributes
    """Method-specific attributes"""

    pending_amount: int
    """Pending amount in cents"""

    related_account_tokens: PaymentTransactionRelatedAccountTokens
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


AccountActivityListResponse: TypeAlias = Union[
    FinancialTransaction,
    BookTransferTransaction,
    CardTransaction,
    PaymentTransaction,
    ExternalPayment,
    ManagementOperationTransaction,
]
