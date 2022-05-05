# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["TransactionSimulateReturnParams"]


class TransactionSimulateReturnParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents) to authorize."""

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""
