# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FinancialAccountChargeOffParams"]


class FinancialAccountChargeOffParams(TypedDict, total=False):
    reason: Required[Literal["DELINQUENT", "FRAUD"]]
    """Reason for the financial account being marked as Charged Off"""
