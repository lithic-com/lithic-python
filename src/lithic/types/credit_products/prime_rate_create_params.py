# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PrimeRateCreateParams"]


class PrimeRateCreateParams(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date the rate goes into effect"""

    rate: Required[str]
    """The rate in decimal format"""
