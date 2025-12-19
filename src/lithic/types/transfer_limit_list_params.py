# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferLimitListParams"]


class TransferLimitListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Date for which to retrieve transfer limits (ISO 8601 format)"""
