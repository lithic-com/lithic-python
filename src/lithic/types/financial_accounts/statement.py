# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..category_details import CategoryDetails
from ..statement_totals import StatementTotals

__all__ = [
    "Statement",
    "AccountStanding",
    "AccountStandingFinancialAccountState",
    "AmountDue",
    "InterestDetails",
    "PayoffDetails",
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


class AmountDue(BaseModel):
    amount: int
    """Payment due at the end of the billing period in cents.

    Negative amount indicates something is owed. If the amount owed is positive
    there was a net credit. If auto-collections are enabled this is the amount that
    will be requested on the payment due date
    """

    past_due: int
    """Amount past due for statement in cents"""


class InterestDetails(BaseModel):
    actual_interest_charged: Optional[int] = None

    daily_balance_amounts: CategoryDetails

    effective_apr: CategoryDetails

    interest_calculation_method: Literal["DAILY", "AVERAGE_DAILY"]

    interest_for_period: CategoryDetails

    prime_rate: Optional[str] = None

    minimum_interest_charged: Optional[int] = None


class PayoffDetails(BaseModel):
    """Details on number and size of payments to pay off balance"""

    minimum_payment_months: str
    """
    The number of months it would take to pay off the balance in full by only paying
    the minimum payment. "NA" will signal negative or zero amortization
    """

    minimum_payment_total: str
    """
    The sum of all interest and principal paid, in cents, when only paying minimum
    monthly payment. "NA" will signal negative or zero amortization
    """

    payoff_period_length_months: Optional[int] = None
    """Number of months to full pay off"""

    payoff_period_monthly_payment_amount: Optional[int] = None
    """
    The amount needed to be paid, in cents, each month in order to pay off current
    balance in the payoff period
    """

    payoff_period_payment_total: Optional[int] = None
    """
    The sum of all interest and principal paid, in cents, when paying off in the
    payoff period
    """


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

    payment_due_date: Optional[date] = None
    """Date when the payment is due"""

    period_totals: StatementTotals

    starting_balance: int
    """Balance at the start of the billing period"""

    statement_end_date: date
    """Date when the billing period ended"""

    statement_start_date: date
    """Date when the billing period began"""

    statement_type: Literal["INITIAL", "PERIOD_END", "FINAL"]

    updated: datetime
    """Timestamp of when the statement was updated"""

    ytd_totals: StatementTotals

    interest_details: Optional[InterestDetails] = None

    next_payment_due_date: Optional[date] = None
    """Date when the next payment is due"""

    next_statement_end_date: Optional[date] = None
    """Date when the next billing period will end"""

    payoff_details: Optional[PayoffDetails] = None
    """Details on number and size of payments to pay off balance"""
