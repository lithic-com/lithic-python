# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ..category_balances import CategoryBalances

__all__ = ["InstallmentPlanStatement", "Installment", "InstallmentPayment"]


class InstallmentPayment(BaseModel):
    amount: int
    """Amount applied to the installment in cents"""

    date: datetime.date
    """Date the payment was applied to the installment"""


class Installment(BaseModel):
    """One installment of a plan as of the statement.

    Amounts are totalled across transaction categories rather than broken out by them, which the installment plan endpoint does
    """

    amount_due: int
    """Amount the installment was opened for in cents"""

    amount_due_details: CategoryBalances

    amount_outstanding: int
    """Amount still owed on the installment in cents"""

    amount_outstanding_details: CategoryBalances

    amount_paid: int
    """Amount paid towards the installment in cents"""

    amount_paid_details: CategoryBalances

    date_assessed: Optional[datetime.date] = None
    """
    Date the installment was actually assessed onto the account, or null if it had
    not been assessed as of this statement
    """

    due_date: datetime.date
    """Date the installment is scheduled to be assessed onto the account"""

    installment_num: int
    """Position of this installment within the plan, starting at 0"""

    payment_due_date: datetime.date
    """Date the installment must be paid by before it is considered past due"""

    payments: List[InstallmentPayment]
    """Payments applied to this installment, oldest first"""


class InstallmentPlanStatement(BaseModel):
    """
    An immutable snapshot of an installment plan as of the statement it is attached to. Lithic cuts one per open plan when a statement is generated and never reissues it
    """

    token: str
    """
    Globally unique identifier for this snapshot, which is the token of the
    statement it is attached to. A plan is snapshotted at most once per statement,
    so the statement identifies the snapshot within the plan. Pass it as a
    pagination cursor
    """

    fee_amount: int
    """Enrollment fee charged when the plan was created in cents"""

    installment_plan_token: str
    """Globally unique identifier for the installment plan this snapshot is of"""

    installment_plan_total: int
    """Total owed on the plan in cents, the principal amount plus the enrollment fee"""

    installments: List[Installment]
    """Installments that make up the plan, oldest first"""

    installments_outstanding: int
    """Number of installments that still carried a balance as of this statement"""

    installments_paid: int
    """Number of installments that had been paid off as of this statement"""

    num_installments: int
    """Number of installments the plan is broken into"""

    principal_amount: int
    """Balance the plan was opened on in cents, excluding the enrollment fee"""

    source_type: Literal["UNPAID_BALANCE", "TRANSACTION"]

    start_date: datetime.date
    """Date the plan was created"""

    state: Literal["PENDING", "ACTIVE", "REBUILD_IN_PROGRESS", "FULLY_PAID", "CANCELLED"]
    """State of the installment plan.

    A plan is REBUILD_IN_PROGRESS while its loan tapes are being rebuilt, during
    which its payment totals are being recomputed and should not be treated as final
    """

    total_paid: int
    """Amount paid towards the plan as of this statement in cents"""
