# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2RetrieveReportParams"]


class V2RetrieveReportParams(TypedDict, total=False):
    begin: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Start date for the report"""

    end: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """End date for the report"""
