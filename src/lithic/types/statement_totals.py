# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["StatementTotals"]


class StatementTotals(BaseModel):
    balance_transfers: int
    """Opening balance transferred from previous account in cents"""

    cash_advances: int
    """ATM and cashback transactions in cents"""

    credits: int
    """
    Volume of credit management operation transactions less any balance transfers in
    cents
    """

    debits: int
    """Volume of debit management operation transactions less any interest in cents"""

    fees: int
    """Volume of debit management operation transactions less any interest in cents"""

    interest: int
    """Interest accrued in cents"""

    payments: int
    """Any funds transfers which affective the balance in cents"""

    purchases: int
    """Net card transaction volume less any cash advances in cents"""

    credit_details: Optional[object] = None
    """Breakdown of credits"""

    debit_details: Optional[object] = None
    """Breakdown of debits"""

    payment_details: Optional[object] = None
    """Breakdown of payments"""
