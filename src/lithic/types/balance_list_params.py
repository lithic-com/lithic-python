# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BalanceListParams"]


class BalanceListParams(TypedDict, total=False):
    account_token: str
    """List balances for all financial accounts of a given account_token."""

    balance_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """UTC date and time of the balances to retrieve.

    Defaults to latest available balances
    """

    business_account_token: str
    """List balances for all financial accounts of a given business_account_token."""

    financial_account_type: Literal["ISSUING", "OPERATING", "RESERVE"]
    """List balances for a given Financial Account type."""
