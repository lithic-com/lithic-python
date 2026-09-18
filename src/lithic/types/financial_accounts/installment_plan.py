# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .transaction_category_balances import TransactionCategoryBalances

__all__ = ["InstallmentPlan", "Installment", "InstallmentPayment"]


class InstallmentPayment(BaseModel):
    amount: int
    """Amount applied to the installment in cents"""

    amount_details: TransactionCategoryBalances

    date: datetime.date
    """Date the payment was applied to the installment"""


class Installment(BaseModel):
    amount_due: int
    """Amount the installment was opened for in cents"""

    amount_due_details: TransactionCategoryBalances

    amount_outstanding: int
    """Amount still owed on the installment in cents"""

    amount_outstanding_details: TransactionCategoryBalances

    amount_paid: int
    """Amount paid towards the installment in cents"""

    amount_paid_details: TransactionCategoryBalances

    date_assessed: Optional[datetime.date] = None
    """
    Date the installment was actually assessed onto the account, or null if it has
    not been assessed yet
    """

    due_date: datetime.date
    """Date the installment is scheduled to be assessed onto the account"""

    installment_num: int
    """Position of this installment within the plan, starting at 0"""

    payment_due_date: datetime.date
    """Date the installment must be paid by before it is considered past due"""

    payments: List[InstallmentPayment]
    """Payments applied to this installment, oldest first"""


class InstallmentPlan(BaseModel):
    token: str
    """Globally unique identifier for an installment plan"""

    closed_at: Optional[datetime.date] = None
    """Date the plan was paid off or cancelled, or null while it is still open"""

    created: datetime.datetime
    """Timestamp of when the installment plan was created"""

    fee_amount: int
    """Enrollment fee charged when the plan was created in cents"""

    financial_account_token: str
    """Globally unique identifier for a financial account"""

    installment_plan_total: int
    """Total owed on the plan in cents, the principal amount plus the enrollment fee"""

    installments: List[Installment]
    """Installments that make up the plan, oldest first"""

    installments_outstanding: int
    """Number of installments that still carry a balance"""

    installments_paid: int
    """Number of installments that have been paid off"""

    num_installments: int
    """Number of installments the plan is broken into"""

    principal_amount: int
    """Balance the plan was opened on in cents, excluding the enrollment fee"""

    source_amounts: Optional[TransactionCategoryBalances] = None
    """
    Balance the plan was opened on, broken out by category, or null if it was not
    recorded
    """

    source_id: str
    """
    Identifier of the record the plan was opened from, such as the closing statement
    for an unpaid balance
    """

    source_type: Literal["UNPAID_BALANCE", "TRANSACTION"]

    start_date: datetime.date
    """Date the plan was created"""

    state: Literal["PENDING", "ACTIVE", "REBUILD_IN_PROGRESS", "FULLY_PAID", "CANCELLED"]
    """State of the installment plan.

    A plan is REBUILD_IN_PROGRESS while its loan tapes are being rebuilt, during
    which its payment totals are being recomputed and should not be treated as final
    """

    total_paid: int
    """Amount paid towards the plan to date in cents"""

    updated: datetime.datetime
    """Timestamp of when the installment plan was updated"""
