# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ..rule_stats import RuleStats

__all__ = ["BacktestResults", "Results", "SimulationParameters"]


class Results(BaseModel):
    current_version: Optional[RuleStats] = None

    draft_version: Optional[RuleStats] = None


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
