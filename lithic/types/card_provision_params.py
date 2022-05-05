# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["CardProvisionParams"]


class CardProvisionParams(TypedDict, total=False):
    account_token: str
    """Only required for multi-account users. Token identifying the account the card will be associated with. Only applicable if using account enrollment. See [Managing Accounts](https://docs.lithic.com/docs/managing-accounts) for more information."""

    certificate: str
    """Required for `APPLE_PAY`. Apple's public leaf certificate. Base64 encoded in PEM format with headers `(-----BEGIN CERTIFICATE-----)` and trailers omitted. Provided by the device's wallet."""

    digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"]
    """Currently `APPLE_PAY` and `SAMSUNG_PAY` are supported (`GOOGLE_PAY` coming soon)."""

    nonce: str
    """Required for `APPLE_PAY`. Base64 cryptographic nonce provided by the device's wallet."""

    nonce_signature: str
    """Required for `APPLE_PAY`. Base64 cryptographic nonce provided by the device's wallet."""
