# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountSpendLimits", "AvailableSpendLimit"]


class AvailableSpendLimit(BaseModel):
    daily: Optional[int] = None
    """
    The available spend limit relative to the daily limit configured on the Account.
    """

    lifetime: Optional[int] = None
    """
    The available spend limit relative to the lifetime limit configured on the
    Account.
    """

    monthly: Optional[int] = None
    """
    The available spend limit relative to the monthly limit configured on the
    Account.
    """


class AccountSpendLimits(BaseModel):
    available_spend_limit: Optional[AvailableSpendLimit] = None

    required: Optional[object] = None
