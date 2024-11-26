# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BacktestCreateResponse"]


class BacktestCreateResponse(BaseModel):
    backtest_token: Optional[str] = None
    """Auth Rule Backtest Token"""
