# File generated from our OpenAPI spec by Stainless.

from datetime import date, datetime

from ..._models import BaseModel

__all__ = ["Statement"]


class Statement(BaseModel):
    token: str
    """Globally unique identifier for a statement"""

    ach_period_total: int
    """Total payments during this billing period."""

    ach_ytd_total: int
    """Year-to-date settled payment total"""

    adjustments_period_total: int
    """Total adjustments during this billing period."""

    adjustments_ytd_total: int
    """Year-to-date settled adjustments total"""

    amount_due: int
    """Payment due at the end of the billing period.

    Negative amount indicates something is owed. If the amount owed is positive
    (e.g., there was a net credit), then payment should be returned to the
    cardholder via ACH.
    """

    available_credit: int
    """Amount of credit available to spend"""

    created: datetime
    """Timestamp of when the statement was created"""

    credit_limit: int
    """For prepay accounts, this is the minimum prepay balance that must be maintained.

    For charge card accounts, this is the maximum credit balance extended by a
    lender.
    """

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

    purchases_period_total: int
    """
    Total settled card transactions during this billing period, determined by
    liability date.
    """

    purchases_ytd_total: int
    """Year-to-date settled card transaction total"""

    starting_balance: int
    """Balance at the start of the billing period"""

    statement_end_date: date
    """Date when the billing period ended"""

    statement_start_date: date
    """Date when the billing period began"""

    updated: datetime
    """Timestamp of when the statement was updated"""
