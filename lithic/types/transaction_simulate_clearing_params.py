# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["TransactionSimulateClearingParams"]


class TransactionSimulateClearingParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize response."""

    amount: int
    """Amount (in cents) to complete. Typically this will match the original authorization, but may be more or less. If no amount is supplied to this endpoint, the amount of the transaction will be captured. Any transaction that has any amount completed at all do not have access to this behavior."""
