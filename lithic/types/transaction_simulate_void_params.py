# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional

from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

__all__ = ["TransactionSimulateVoidParams"]


class TransactionSimulateVoidParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize response."""

    amount: int
    """Amount (in cents) to void.

    Typically this will match the original authorization, but may be less.
    """
