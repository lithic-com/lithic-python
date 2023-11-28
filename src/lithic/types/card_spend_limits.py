# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["CardSpendLimits", "AvailableSpendLimit"]


class AvailableSpendLimit(BaseModel):
    annually: Optional[int] = None
    """The available spend limit relative to the annual limit configured on the Card."""

    forever: Optional[int] = None
    """The available spend limit relative to the forever limit configured on the Card."""

    monthly: Optional[int] = None
    """The available spend limit relative to the monthly limit configured on the Card."""


class CardSpendLimits(BaseModel):
    available_spend_limit: Optional[AvailableSpendLimit] = None

    required: Optional[object] = None
