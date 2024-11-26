# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

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
    """Whether the rule would have approved the authorization request."""

    event_token: Optional[str] = None
    """The authorization request event token."""

    timestamp: Optional[datetime] = None
    """The timestamp of the authorization request event."""


class ResultsCurrentVersion(BaseModel):
    approved: Optional[int] = None
    """
    The total number of historical transactions approved by this rule during the
    backtest period, or the number of transactions that would have been approved if
    the rule was evaluated in shadow mode.
    """

    declined: Optional[int] = None
    """
    The total number of historical transactions declined by this rule during the
    backtest period, or the number of transactions that would have been declined if
    the rule was evaluated in shadow mode.
    """

    examples: Optional[List[ResultsCurrentVersionExample]] = None
    """Example authorization request events that would have been approved or declined."""

    version: Optional[int] = None
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class ResultsDraftVersionExample(BaseModel):
    approved: Optional[bool] = None
    """Whether the rule would have approved the authorization request."""

    event_token: Optional[str] = None
    """The authorization request event token."""

    timestamp: Optional[datetime] = None
    """The timestamp of the authorization request event."""


class ResultsDraftVersion(BaseModel):
    approved: Optional[int] = None
    """
    The total number of historical transactions approved by this rule during the
    backtest period, or the number of transactions that would have been approved if
    the rule was evaluated in shadow mode.
    """

    declined: Optional[int] = None
    """
    The total number of historical transactions declined by this rule during the
    backtest period, or the number of transactions that would have been declined if
    the rule was evaluated in shadow mode.
    """

    examples: Optional[List[ResultsDraftVersionExample]] = None
    """Example authorization request events that would have been approved or declined."""

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
