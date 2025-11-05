# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FinancialAccountCreditConfig", "AutoCollectionConfiguration"]


class AutoCollectionConfiguration(BaseModel):
    auto_collection_enabled: bool
    """If auto collection is enabled for this account"""


class FinancialAccountCreditConfig(BaseModel):
    account_token: str
    """Globally unique identifier for the account"""

    auto_collection_configuration: AutoCollectionConfiguration

    credit_limit: Optional[int] = None

    credit_product_token: Optional[str] = None
    """Globally unique identifier for the credit product"""

    external_bank_account_token: Optional[str] = None

    tier: Optional[str] = None
    """Tier assigned to the financial account"""
