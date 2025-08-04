# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .transaction import Transaction
from .external_payment import ExternalPayment
from .external_resource import ExternalResource
from .management_operation_transaction import ManagementOperationTransaction

__all__ = [
    "AccountActivityRetrieveTransactionResponse",
    "FinancialTransaction",
    "BookTransferTransaction",
    "BookTransferTransactionTransactionSeries",
    "CardTransaction",
    "PaymentTransaction",
    "PaymentTransactionMethodAttributes",
    "PaymentTransactionMethodAttributesACHMethodAttributes",
    "PaymentTransactionMethodAttributesWireMethodAttributes",
    "PaymentTransactionRelatedAccountTokens",
]


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

    events: List[object]
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

    events: List[object]
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
    wire_transfer_type: Literal["FEDWIRE", "SWIFT"]
    """Type of wire transfer"""

    external_bank_name: Optional[str] = None
    """External bank name"""

    external_bank_routing_number: Optional[str] = None
    """External bank routing number"""

    external_individual_name: Optional[str] = None
    """External individual name"""

    lithic_bank_name: Optional[str] = None
    """Lithic bank name"""

    lithic_bank_routing_number: Optional[str] = None
    """Lithic bank routing number"""

    lithic_individual_name: Optional[str] = None
    """Lithic individual name"""

    previous_transfer: Optional[str] = None
    """UUID of previous transfer if this is a retry"""


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

    events: List[object]
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

    user_defined_id: Optional[str] = None
    """User-defined identifier"""


AccountActivityRetrieveTransactionResponse: TypeAlias = Union[
    FinancialTransaction,
    BookTransferTransaction,
    CardTransaction,
    PaymentTransaction,
    ExternalPayment,
    ManagementOperationTransaction,
]
