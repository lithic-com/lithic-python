# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["FundingSourceVerifyParams"]


class FundingSourceVerifyParams(TypedDict, total=False):
    micro_deposits: Required[List[int]]
    """An array of dollar amounts (in cents) received in two credit transactions."""

    account_token: str
    """Only required for multi-account users. Token identifying the account that the bank account will be associated with. Only applicable if using account enrollment. See [Managing Accounts](https://docs.lithic.com/docs/managing-accounts) for more information."""
