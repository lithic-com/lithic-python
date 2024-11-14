# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PrimeRateRetrieveParams"]


class PrimeRateRetrieveParams(TypedDict, total=False):
    ending_before: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The effective date that the prime rates ends before"""

    starting_after: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The effective date that the prime rate starts after"""
