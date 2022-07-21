# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FundingSourceUpdateParams"]


class FundingSourceUpdateParams(TypedDict, total=False):
    account_token: str
    """Only required for multi-account users.

    Token identifying the account that the bank account will be associated with.
    Only applicable if using account holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """

    state: Literal["DELETED", "ENABLED"]
    """The desired state of the bank account.

    If a bank account is set to `DELETED`, all cards linked to this account will no
    longer be associated with it. If there are no other bank accounts in state
    `ENABLED` on the account, authorizations will not be accepted on the card until
    a new funding account is added.
    """
