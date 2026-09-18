# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .category_balances import CategoryBalances

__all__ = ["TransactionCategoryBalances"]


class TransactionCategoryBalances(BaseModel):
    balance_transfers: CategoryBalances
    """Amounts attributable to balance transfers"""

    cash_advances: CategoryBalances
    """Amounts attributable to cash advances"""

    purchases: CategoryBalances
    """Amounts attributable to purchases"""
