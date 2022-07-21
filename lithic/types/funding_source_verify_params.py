# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FundingSourceVerifyParams"]


class FundingSourceVerifyParams(TypedDict, total=False):
    micro_deposits: Required[List[int]]
    """An array of dollar amounts (in cents) received in two credit transactions."""

    account_token: str
    """Only required for multi-account users.

    Token identifying the account that the bank account will be associated with.
    Only applicable if using account holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """
