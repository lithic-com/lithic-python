# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FinancialAccount", "CreditConfiguration"]


class CreditConfiguration(BaseModel):
    credit_limit: Optional[int] = None

    credit_product_token: Optional[str] = None
    """Globally unique identifier for the credit product"""

    external_bank_account_token: Optional[str] = None

    tier: Optional[str] = None
    """Tier assigned to the financial account"""

    financial_account_state: Optional[Literal["PENDING", "CURRENT", "DELINQUENT"]] = None
    """State of the financial account"""


class FinancialAccount(BaseModel):
    token: str
    """Globally unique identifier for the account"""

    account_token: Optional[str] = None

    created: datetime

    credit_configuration: Optional[CreditConfiguration] = None

    is_for_benefit_of: bool
    """Whether financial account is for the benefit of another entity"""

    nickname: Optional[str] = None

    type: Literal["ISSUING", "RESERVE", "OPERATING"]

    updated: datetime

    account_number: Optional[str] = None

    routing_number: Optional[str] = None
