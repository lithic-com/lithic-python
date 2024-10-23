# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "Statement",
    "AccountStanding",
    "AmountDue",
    "PeriodTotals",
    "YtdTotals",
    "InterestDetails",
    "InterestDetailsDailyBalanceAmounts",
    "InterestDetailsEffectiveApr",
    "InterestDetailsInterestForPeriod",
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


class AmountDue(BaseModel):
    amount: int
    """Payment due at the end of the billing period in cents.

    Negative amount indicates something is owed. If the amount owed is positive
    there was a net credit. If auto-collections are enabled this is the amount that
    will be requested on the payment due date
    """

    past_due: int
    """Amount past due for statement in cents"""


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


class InterestDetailsDailyBalanceAmounts(BaseModel):
    balance_transfers: str

    cash_advances: str

    purchases: str


class InterestDetailsEffectiveApr(BaseModel):
    balance_transfers: str

    cash_advances: str

    purchases: str


class InterestDetailsInterestForPeriod(BaseModel):
    balance_transfers: str

    cash_advances: str

    purchases: str


class InterestDetails(BaseModel):
    actual_interest_charged: Optional[int] = None

    daily_balance_amounts: InterestDetailsDailyBalanceAmounts

    effective_apr: InterestDetailsEffectiveApr

    interest_calculation_method: Literal["DAILY", "AVERAGE_DAILY"]

    interest_for_period: InterestDetailsInterestForPeriod

    prime_rate: Optional[str] = None

    minimum_interest_charged: Optional[int] = None


class Statement(BaseModel):
    token: str
    """Globally unique identifier for a statement"""

    account_standing: AccountStanding

    amount_due: AmountDue

    available_credit: int
    """Amount of credit available to spend in cents"""

    created: datetime
    """Timestamp of when the statement was created"""

    credit_limit: int
    """This is the maximum credit balance extended by the lender in cents"""

    credit_product_token: str
    """Globally unique identifier for a credit product"""

    days_in_billing_cycle: int
    """Number of days in the billing cycle"""

    ending_balance: int
    """Balance at the end of the billing period.

    For charge cards, this should be the same at the statement amount due in cents
    """

    financial_account_token: str
    """Globally unique identifier for a financial account"""

    payment_due_date: date
    """Date when the payment is due"""

    period_totals: PeriodTotals

    starting_balance: int
    """Balance at the start of the billing period"""

    statement_end_date: date
    """Date when the billing period ended"""

    statement_start_date: date
    """Date when the billing period began"""

    statement_type: Literal["INITIAL", "PERIOD_END"]

    updated: datetime
    """Timestamp of when the statement was updated"""

    ytd_totals: YtdTotals

    interest_details: Optional[InterestDetails] = None

    next_payment_due_date: Optional[date] = None
    """Date when the next payment is due"""

    next_statement_end_date: Optional[date] = None
    """Date when the next billing period will end"""
