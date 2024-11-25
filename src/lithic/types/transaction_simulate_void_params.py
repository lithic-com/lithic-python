# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransactionSimulateVoidParams"]


class TransactionSimulateVoidParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize response."""

    amount: int
    """Amount (in cents) to void.

    Typically this will match the amount in the original authorization, but can be
    less.
    """

    type: Literal["AUTHORIZATION_EXPIRY", "AUTHORIZATION_REVERSAL"]
    """Type of event to simulate. Defaults to `AUTHORIZATION_REVERSAL`.

    - `AUTHORIZATION_EXPIRY` indicates authorization has expired and been reversed
      by Lithic.
    - `AUTHORIZATION_REVERSAL` indicates authorization was reversed by the merchant.
    """
