# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenizationSimulateParams"]


class TokenizationSimulateParams(TypedDict, total=False):
    cvv: Required[str]
    """The three digit cvv for the card."""

    expiration_date: Required[str]
    """The expiration date of the card in 'MM/YY' format."""

    pan: Required[str]
    """The sixteen digit card number."""

    tokenization_source: Required[Literal["APPLE_PAY", "GOOGLE", "SAMSUNG_PAY", "MERCHANT"]]
    """The source of the tokenization request."""

    account_score: int
    """
    The account score (1-5) that represents how the Digital Wallet's view on how
    reputable an end user's account is.
    """

    device_score: int
    """
    The device score (1-5) that represents how the Digital Wallet's view on how
    reputable an end user's device is.
    """

    entity: str
    """
    Optional field to specify the token requestor name for a merchant token
    simulation. Ignored when tokenization_source is not MERCHANT.
    """

    wallet_recommended_decision: Literal["APPROVED", "DECLINED", "REQUIRE_ADDITIONAL_AUTHENTICATION"]
    """The decision that the Digital Wallet's recommend"""
