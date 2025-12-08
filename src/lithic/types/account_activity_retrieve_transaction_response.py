# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .payment import Payment
from .._models import BaseModel
from .transaction import Transaction
from .external_payment import ExternalPayment
from .book_transfer_response import BookTransferResponse
from .shared.financial_event import FinancialEvent
from .management_operation_transaction import ManagementOperationTransaction

__all__ = ["AccountActivityRetrieveTransactionResponse", "FinancialTransaction", "CardTransaction"]


class FinancialTransaction(BaseModel):
    """Financial transaction with inheritance from unified base transaction"""

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
        "EXTERNAL_FEDNOW",
        "EXTERNAL_RTP",
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

    events: List[FinancialEvent]
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

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED", "RETURNED"]
    """The status of the transaction"""

    updated: datetime
    """ISO 8601 timestamp of when the transaction was last updated"""


class CardTransaction(Transaction):
    """Card transaction with ledger base properties"""

    token: str  # type: ignore
    """Unique identifier for the transaction"""

    created: datetime  # type: ignore
    """ISO 8601 timestamp of when the transaction was created"""

    family: Literal["CARD"]
    """CARD - Card Transaction"""

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED", "RETURNED"]  # type: ignore
    """The status of the transaction"""

    updated: datetime  # type: ignore
    """ISO 8601 timestamp of when the transaction was last updated"""


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
