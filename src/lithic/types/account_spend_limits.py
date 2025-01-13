# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountSpendLimits", "AvailableSpendLimit", "SpendLimit", "SpendVelocity"]


class AvailableSpendLimit(BaseModel):
    daily: Optional[int] = None
    """
    The available spend limit (in cents) relative to the daily limit configured on
    the Account (e.g. 100000 would be a $1,000 limit).
    """

    lifetime: Optional[int] = None
    """
    The available spend limit (in cents) relative to the lifetime limit configured
    on the Account.
    """

    monthly: Optional[int] = None
    """
    The available spend limit (in cents) relative to the monthly limit configured on
    the Account.
    """


class SpendLimit(BaseModel):
    daily: Optional[int] = None
    """The configured daily spend limit (in cents) on the Account."""

    lifetime: Optional[int] = None
    """The configured lifetime spend limit (in cents) on the Account."""

    monthly: Optional[int] = None
    """The configured monthly spend limit (in cents) on the Account."""


class SpendVelocity(BaseModel):
    daily: Optional[int] = None
    """Current daily spend velocity (in cents) on the Account.

    Present if daily spend limit is set.
    """

    lifetime: Optional[int] = None
    """Current lifetime spend velocity (in cents) on the Account.

    Present if lifetime spend limit is set.
    """

    monthly: Optional[int] = None
    """Current monthly spend velocity (in cents) on the Account.

    Present if monthly spend limit is set.
    """


class AccountSpendLimits(BaseModel):
    available_spend_limit: AvailableSpendLimit

    spend_limit: Optional[SpendLimit] = None

    spend_velocity: Optional[SpendVelocity] = None
