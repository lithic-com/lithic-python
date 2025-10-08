# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FinancialAccountCreditConfig", "AutoCollectionConfiguration"]


class AutoCollectionConfiguration(BaseModel):
    auto_collection_enabled: bool
    """If auto collection is enabled for this account"""


class FinancialAccountCreditConfig(BaseModel):
    account_token: str
    """Globally unique identifier for the account"""

    auto_collection_configuration: AutoCollectionConfiguration

    charged_off_reason: Optional[Literal["DELINQUENT", "FRAUD"]] = None
    """Reason for the financial account being marked as Charged Off"""

    credit_limit: Optional[int] = None

    credit_product_token: Optional[str] = None
    """Globally unique identifier for the credit product"""

    external_bank_account_token: Optional[str] = None

    financial_account_state: Literal["PENDING", "CURRENT", "DELINQUENT", "CHARGED_OFF"]
    """State of the financial account"""

    is_spend_blocked: bool

    tier: Optional[str] = None
    """Tier assigned to the financial account"""
