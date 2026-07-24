# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BalanceListParams"]


class BalanceListParams(TypedDict, total=False):
    balance_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """UTC date of the balance to retrieve. Defaults to latest available balance"""

    last_transaction_event_token: str
    """
    Balance after a given financial event occured. Note: if an account receives
    multiple events around the same time whose financial impacts cancel out, a
    balance lookup by one of those event tokens may return 404, since their combined
    impact on the account is zero.
    """
