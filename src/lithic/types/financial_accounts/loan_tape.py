# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "LoanTape",
    "AccountStanding",
    "BalanceDue",
    "BalanceNextDue",
    "BalancePastDue",
    "DayTotals",
    "MinimumPaymentBalance",
    "PaymentAllocation",
    "PeriodTotals",
    "PreviousStatementBalance",
    "YtdTotals",
]


class AccountStanding(BaseModel):
    consecutive_full_payments_made: int
    """Number of consecutive full payments made"""

    consecutive_minimum_payments_made: int
    """Number of consecutive minimum payments made"""

    consecutive_minimum_payments_missed: int
    """Number of consecutive minimum payments missed"""

    days_past_due: int
    """Number of days past due"""

    has_grace: bool
    """Whether the account currently has grace or not"""

    period_number: int
    """Current overall period number"""

    period_state: Literal["STANDARD", "PROMO", "PENALTY"]


class BalanceDue(BaseModel):
    fees: int

    interest: int

    principal: int


class BalanceNextDue(BaseModel):
    fees: int

    interest: int

    principal: int


class BalancePastDue(BaseModel):
    fees: int

    interest: int

    principal: int


class DayTotals(BaseModel):
    balance_transfers: int
    """Opening balance transferred from previous account in cents"""

    cash_advances: int
    """ATM and cashback transactions in cents"""

    credits: int
    """
    Volume of credit management operation transactions less any balance transfers in
    cents
    """

    fees: int
    """Volume of debit management operation transactions less any interest in cents"""

    interest: int
    """Interest accrued in cents"""

    payments: int
    """Any funds transfers which affective the balance in cents"""

    purchases: int
    """Net card transaction volume less any cash advances in cents"""


class MinimumPaymentBalance(BaseModel):
    amount: int

    remaining: int


class PaymentAllocation(BaseModel):
    fees: int

    interest: int

    principal: int


class PeriodTotals(BaseModel):
    balance_transfers: int
    """Opening balance transferred from previous account in cents"""

    cash_advances: int
    """ATM and cashback transactions in cents"""

    credits: int
    """
    Volume of credit management operation transactions less any balance transfers in
    cents
    """

    fees: int
    """Volume of debit management operation transactions less any interest in cents"""

    interest: int
    """Interest accrued in cents"""

    payments: int
    """Any funds transfers which affective the balance in cents"""

    purchases: int
    """Net card transaction volume less any cash advances in cents"""


class PreviousStatementBalance(BaseModel):
    amount: int

    remaining: int


class YtdTotals(BaseModel):
    balance_transfers: int
    """Opening balance transferred from previous account in cents"""

    cash_advances: int
    """ATM and cashback transactions in cents"""

    credits: int
    """
    Volume of credit management operation transactions less any balance transfers in
    cents
    """

    fees: int
    """Volume of debit management operation transactions less any interest in cents"""

    interest: int
    """Interest accrued in cents"""

    payments: int
    """Any funds transfers which affective the balance in cents"""

    purchases: int
    """Net card transaction volume less any cash advances in cents"""


class LoanTape(BaseModel):
    token: str
    """Globally unique identifier for a loan tape"""

    account_standing: AccountStanding

    available_credit: int
    """Amount of credit available to spend in cents"""

    balance_due: BalanceDue
    """Amount due for the prior billing cycle.

    Any amounts not fully paid off on this due date will be considered past due the
    next day
    """

    balance_next_due: BalanceNextDue
    """Amount due for the current billing cycle.

    Any amounts not paid off by early payments or credits will be considered due at
    the end of the current billing period
    """

    balance_past_due: BalancePastDue
    """Amount not paid off on previous due dates"""

    created: datetime.datetime
    """Timestamp of when the loan tape was created"""

    credit_limit: int
    """For prepay accounts, this is the minimum prepay balance that must be maintained.

    For charge card accounts, this is the maximum credit balance extended by a
    lender
    """

    credit_product_token: str
    """Globally unique identifier for a credit product"""

    date: datetime.date
    """Date of transactions that this loan tape covers"""

    day_totals: DayTotals

    ending_balance: int
    """Balance at the end of the day"""

    excess_credits: int
    """Excess credits in the form of provisional credits, payments, or purchase
    refunds.

    If positive, the account is in net credit state with no outstanding balances. An
    overpayment could land an account in this state
    """

    financial_account_token: str
    """Globally unique identifier for a financial account"""

    minimum_payment_balance: MinimumPaymentBalance

    payment_allocation: PaymentAllocation

    period_totals: PeriodTotals

    previous_statement_balance: PreviousStatementBalance

    starting_balance: int
    """Balance at the start of the day"""

    updated: datetime.datetime
    """Timestamp of when the loan tape was updated"""

    version: int
    """Version number of the loan tape. This starts at 1"""

    ytd_totals: YtdTotals

    tier: Optional[str] = None
    """Interest tier to which this account belongs to"""
