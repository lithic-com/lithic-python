# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ..backtest_stats import BacktestStats

__all__ = ["BacktestResults", "Results", "SimulationParameters"]


class Results(BaseModel):
    current_version: Optional[BacktestStats] = None

    draft_version: Optional[BacktestStats] = None


class SimulationParameters(BaseModel):
    end: datetime
    """The end time of the simulation"""

    start: datetime
    """The start time of the simulation"""


class BacktestResults(BaseModel):
    backtest_token: str
    """Auth Rule Backtest Token"""

    results: Results

    simulation_parameters: SimulationParameters
