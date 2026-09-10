# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentCreateStablecoinParams", "Hold"]


class PaymentCreateStablecoinParams(TypedDict, total=False):
    amount: Required[int]
    """Payout amount in cents"""

    blockchain_recipient_token: Required[str]
    """Token of the blockchain recipient to send the payout to.

    The recipient must be in the `ENABLED` verification state
    """

    financial_account_token: Required[str]
    """Token of the financial account the payout is funded from"""

    type: Required[Literal["PAYMENT"]]
    """Direction of the payment. Stablecoin supports payouts only"""

    token: str
    """Customer-provided token that will serve as an idempotency token.

    This token will become the transaction token
    """

    hold: Hold
    """Optional hold to settle when this payout is initiated"""

    memo: str
    """Memo recorded on the payout.

    Defaults to `Stablecoin payout on <chain>` when omitted
    """


class Hold(TypedDict, total=False):
    """Optional hold to settle when this payout is initiated"""

    token: Required[str]
    """Token of the hold to settle when this payout is initiated"""
