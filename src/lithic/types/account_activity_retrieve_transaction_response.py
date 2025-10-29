# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .payment import Payment
from .._models import BaseModel
from .transaction import Transaction
from .external_payment import ExternalPayment
from .book_transfer_response import BookTransferResponse
from .management_operation_transaction import ManagementOperationTransaction

__all__ = [
    "AccountActivityRetrieveTransactionResponse",
    "FinancialTransaction",
    "FinancialTransactionEvent",
    "CardTransaction",
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
            "ACH_ORIGINATION_REJECTED",
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_PROCESSED",
            "ACH_RECEIPT_RELEASED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_REJECTED",
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

    currency: str
    """Currency of the transaction, represented in ISO 4217 format"""

    descriptor: str
    """Transaction descriptor"""

    events: List[FinancialTransactionEvent]
    """List of transaction events"""

    family: Literal["INTERNAL"]
    """INTERNAL - Financial Transaction"""

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


class CardTransaction(Transaction):
    pass


AccountActivityRetrieveTransactionResponse: TypeAlias = Annotated[
    Union[
        FinancialTransaction,
        BookTransferResponse,
        CardTransaction,
        Payment,
        ExternalPayment,
        ManagementOperationTransaction,
    ],
    PropertyInfo(discriminator="family"),
]
