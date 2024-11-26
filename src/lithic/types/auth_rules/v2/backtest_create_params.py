# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BacktestCreateParams"]


class BacktestCreateParams(TypedDict, total=False):
    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end time of the backtest."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The start time of the backtest."""
