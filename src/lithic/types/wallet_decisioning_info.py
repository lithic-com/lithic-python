# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WalletDecisioningInfo"]


class WalletDecisioningInfo(BaseModel):
    account_score: Optional[str] = None
    """Score given to the account by the Wallet Provider"""

    device_score: Optional[str] = None
    """Score given to the device by the Wallet Provider"""

    recommended_decision: Optional[str] = None
    """The decision recommended by the Wallet Provider"""

    recommendation_reasons: Optional[List[str]] = None
    """
    Reasons provided to the Wallet Provider on how the recommended decision was
    reached
    """
