# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Statement", "AccountStanding", "PeriodTotals", "YtdTotals"]


class AccountStanding(BaseModel):
    period_number: int
    """Current overall period number"""

    state: Literal["STANDARD", "PROMO", "PENALTY"]


class PeriodTotals(BaseModel):
    balance_transfers: int

    cash_advances: int

    credits: int

    fees: int

    interest: int

    payments: int

    purchases: int


class YtdTotals(BaseModel):
    balance_transfers: int

    cash_advances: int

    credits: int

    fees: int

    interest: int

    payments: int

    purchases: int


class Statement(BaseModel):
    token: str
    """Globally unique identifier for a statement"""

    account_standing: AccountStanding

    amount_due: int
    """Payment due at the end of the billing period.

    Negative amount indicates something is owed. If the amount owed is positive
    (e.g., there was a net credit), then payment should be returned to the
    cardholder via ACH.
    """

    amount_past_due: int
    """Payment past due at the end of the billing period."""

    available_credit: int
    """Amount of credit available to spend"""

    created: datetime
    """Timestamp of when the statement was created"""

    credit_limit: int
    """For prepay accounts, this is the minimum prepay balance that must be maintained.

    For charge card accounts, this is the maximum credit balance extended by a
    lender.
    """

    credit_product_token: str
    """Globally unique identifier for a credit product"""

    days_in_billing_cycle: int
    """Number of days in the billing cycle"""

    ending_balance: int
    """Balance at the end of the billing period.

    For charge cards, this should be the same at the statement amount due.
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

    updated: datetime
    """Timestamp of when the statement was updated"""

    ytd_totals: YtdTotals
