# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FinancialAccountCreditConfig"]


class FinancialAccountCreditConfig(BaseModel):
    account_token: str
    """Globally unique identifier for the account"""

    credit_limit: Optional[int] = None

    credit_product_token: Optional[str] = None
    """Globally unique identifier for the credit product"""

    external_bank_account_token: Optional[str] = None

    tier: Optional[str] = None
    """Tier assigned to the financial account"""

    financial_account_state: Optional[Literal["PENDING", "CURRENT", "DELINQUENT"]] = None
    """State of the financial account"""

    is_spend_blocked: Optional[bool] = None
