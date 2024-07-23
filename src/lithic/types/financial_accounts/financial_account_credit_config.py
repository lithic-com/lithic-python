# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FinancialAccountCreditConfig"]


class FinancialAccountCreditConfig(BaseModel):
    account_token: str
    """Globally unique identifier for the account"""

    credit_limit: Optional[int] = None

    credit_product_token: Optional[str] = None
    """Globally unique identifier for the credit product"""

    external_bank_account_token: Optional[str] = None
