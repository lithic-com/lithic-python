# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .financial_account_balance import FinancialAccountBalance

__all__ = ["BalanceUpdatedWebhookEvent"]


class BalanceUpdatedWebhookEvent(BaseModel):
    data: List[FinancialAccountBalance]

    event_type: Literal["balance.updated"]
    """The type of event that occurred."""
