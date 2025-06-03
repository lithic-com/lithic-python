# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "BacktestResults",
    "Results",
    "ResultsCurrentVersion",
    "ResultsCurrentVersionExample",
    "ResultsDraftVersion",
    "ResultsDraftVersionExample",
    "SimulationParameters",
]


class ResultsCurrentVersionExample(BaseModel):
    approved: Optional[bool] = None
    """Whether the rule would have approved the request."""

    decision: Optional[Literal["APPROVED", "DECLINED", "CHALLENGED"]] = None
    """The decision made by the rule for this event."""

    event_token: Optional[str] = None
    """The event token."""

    timestamp: Optional[datetime] = None
    """The timestamp of the event."""


class ResultsCurrentVersion(BaseModel):
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

    examples: Optional[List[ResultsCurrentVersionExample]] = None
    """Example events and their outcomes."""

    version: Optional[int] = None
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class ResultsDraftVersionExample(BaseModel):
    approved: Optional[bool] = None
    """Whether the rule would have approved the request."""

    decision: Optional[Literal["APPROVED", "DECLINED", "CHALLENGED"]] = None
    """The decision made by the rule for this event."""

    event_token: Optional[str] = None
    """The event token."""

    timestamp: Optional[datetime] = None
    """The timestamp of the event."""


class ResultsDraftVersion(BaseModel):
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

    examples: Optional[List[ResultsDraftVersionExample]] = None
    """Example events and their outcomes."""

    version: Optional[int] = None
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class Results(BaseModel):
    current_version: Optional[ResultsCurrentVersion] = None

    draft_version: Optional[ResultsDraftVersion] = None


class SimulationParameters(BaseModel):
    auth_rule_token: Optional[str] = None
    """Auth Rule Token"""

    end: Optional[datetime] = None
    """The end time of the simulation."""

    start: Optional[datetime] = None
    """The start time of the simulation."""


class BacktestResults(BaseModel):
    backtest_token: str
    """Auth Rule Backtest Token"""

    results: Results

    simulation_parameters: SimulationParameters
