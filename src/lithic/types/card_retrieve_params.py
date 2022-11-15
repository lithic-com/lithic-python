# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CardRetrieveParams"]


class CardRetrieveParams(TypedDict, total=False):
    account_token: str
    """Only required for multi-account users using account holder enrollment.

    Returns card associated with this account. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """
