# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..category_details import CategoryDetails
from ..statement_totals import StatementTotals
from .category_balances import CategoryBalances

__all__ = [
    "LoanTape",
    "AccountStanding",
    "AccountStandingFinancialAccountState",
    "Balances",
    "InterestDetails",
    "MinimumPaymentBalance",
    "PaymentAllocation",
    "PreviousStatementBalance",
]


class AccountStandingFinancialAccountState(BaseModel):
    """Information about the financial account state"""

    status: Literal["OPEN", "CLOSED", "SUSPENDED", "PENDING"]
    """Status of the financial account"""

    substatus: Optional[
        Literal["CHARGED_OFF_DELINQUENT", "CHARGED_OFF_FRAUD", "END_USER_REQUEST", "BANK_REQUEST", "DELINQUENT"]
    ] = None
    """Substatus for the financial account"""


class AccountStanding(BaseModel):
    consecutive_full_payments_made: int
    """Number of consecutive full payments made"""

    consecutive_minimum_payments_made: int
    """Number of consecutive minimum payments made"""

    consecutive_minimum_payments_missed: int
    """Number of consecutive minimum payments missed"""

    days_past_due: int
    """Number of days past due"""

    financial_account_state: AccountStandingFinancialAccountState
    """Information about the financial account state"""

    has_grace: bool
    """Whether the account currently has grace or not"""

    period_number: int
    """Current overall period number"""

    period_state: Literal["STANDARD", "PROMO", "PENALTY"]


class Balances(BaseModel):
    due: CategoryBalances
    """Amount due for the prior billing cycle.

    Any amounts not fully paid off on this due date will be considered past due the
    next day
    """

    next_statement_due: CategoryBalances
    """Amount due for the current billing cycle.

    Any amounts not paid off by early payments or credits will be considered due at
    the end of the current billing period
    """

    past_due: CategoryBalances
    """Amount not paid off on previous due dates"""

    past_statements_due: CategoryBalances
    """Amount due for the past billing cycles."""


class InterestDetails(BaseModel):
    actual_interest_charged: Optional[int] = None

    daily_balance_amounts: CategoryDetails

    effective_apr: CategoryDetails

    interest_calculation_method: Literal["DAILY", "AVERAGE_DAILY"]

    interest_for_period: CategoryDetails

    prime_rate: Optional[str] = None

    minimum_interest_charged: Optional[int] = None


class MinimumPaymentBalance(BaseModel):
    amount: int

    remaining: int


class PaymentAllocation(BaseModel):
    fee_details: Optional[CategoryDetails] = None

    fees: int
    """Amount allocated to fees in cents"""

    interest: int
    """Amount allocated to interest in cents"""

    interest_details: Optional[CategoryDetails] = None

    principal: int
    """Amount allocated to principal in cents"""

    principal_details: Optional[CategoryDetails] = None


class PreviousStatementBalance(BaseModel):
    amount: int

    remaining: int


class LoanTape(BaseModel):
    token: str
    """Globally unique identifier for a loan tape"""

    account_standing: AccountStanding

    available_credit: int
    """Amount of credit available to spend in cents"""

    balances: Balances

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

    day_totals: StatementTotals

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

    interest_details: Optional[InterestDetails] = None

    minimum_payment_balance: MinimumPaymentBalance

    payment_allocation: PaymentAllocation

    period_totals: StatementTotals

    previous_statement_balance: PreviousStatementBalance

    starting_balance: int
    """Balance at the start of the day"""

    updated: datetime.datetime
    """Timestamp of when the loan tape was updated"""

    version: int
    """Version number of the loan tape. This starts at 1"""

    ytd_totals: StatementTotals

    tier: Optional[str] = None
    """Interest tier to which this account belongs to"""
