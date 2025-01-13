# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CardSpendLimits", "AvailableSpendLimit", "SpendLimit", "SpendVelocity"]


class AvailableSpendLimit(BaseModel):
    annually: Optional[int] = None
    """
    The available spend limit (in cents) relative to the annual limit configured on
    the Card (e.g. 100000 would be a $1,000 limit).
    """

    forever: Optional[int] = None
    """
    The available spend limit (in cents) relative to the forever limit configured on
    the Card.
    """

    monthly: Optional[int] = None
    """
    The available spend limit (in cents) relative to the monthly limit configured on
    the Card.
    """


class SpendLimit(BaseModel):
    annually: Optional[int] = None
    """The configured annual spend limit (in cents) on the Card."""

    forever: Optional[int] = None
    """The configured forever spend limit (in cents) on the Card."""

    monthly: Optional[int] = None
    """The configured monthly spend limit (in cents) on the Card."""


class SpendVelocity(BaseModel):
    annually: Optional[int] = None
    """Current annual spend velocity (in cents) on the Card.

    Present if annual spend limit is set.
    """

    forever: Optional[int] = None
    """Current forever spend velocity (in cents) on the Card.

    Present if forever spend limit is set.
    """

    monthly: Optional[int] = None
    """Current monthly spend velocity (in cents) on the Card.

    Present if monthly spend limit is set.
    """


class CardSpendLimits(BaseModel):
    available_spend_limit: AvailableSpendLimit

    spend_limit: Optional[SpendLimit] = None

    spend_velocity: Optional[SpendVelocity] = None
