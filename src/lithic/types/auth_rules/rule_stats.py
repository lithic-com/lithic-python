# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RuleStats", "Example"]


class Example(BaseModel):
    approved: Optional[bool] = None
    """Whether the rule would have approved the request."""

    decision: Optional[Literal["APPROVED", "DECLINED", "CHALLENGED"]] = None
    """The decision made by the rule for this event."""

    event_token: Optional[str] = None
    """The event token."""

    timestamp: Optional[datetime] = None
    """The timestamp of the event."""


class RuleStats(BaseModel):
    approved: Optional[int] = None
    """
    The total number of historical transactions approved by this rule during the
    relevant period, or the number of transactions that would have been approved if
    the rule was evaluated in shadow mode.
    """

    challenged: Optional[int] = None
    """
    The total number of historical transactions challenged by this rule during the
    relevant period, or the number of transactions that would have been challenged
    if the rule was evaluated in shadow mode. Currently applicable only for 3DS Auth
    Rules.
    """

    declined: Optional[int] = None
    """
    The total number of historical transactions declined by this rule during the
    relevant period, or the number of transactions that would have been declined if
    the rule was evaluated in shadow mode.
    """

    examples: Optional[List[Example]] = None
    """Example events and their outcomes."""

    version: Optional[int] = None
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """
