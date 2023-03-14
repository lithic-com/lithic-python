# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardProvisionParams"]


class CardProvisionParams(TypedDict, total=False):
    certificate: str
    """Required for `APPLE_PAY`.

    Apple's public leaf certificate. Base64 encoded in PEM format with headers
    `(-----BEGIN CERTIFICATE-----)` and trailers omitted. Provided by the device's
    wallet.
    """

    digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"]
    """Name of digital wallet provider."""

    nonce: str
    """Required for `APPLE_PAY`.

    Base64 cryptographic nonce provided by the device's wallet.
    """

    nonce_signature: str
    """Required for `APPLE_PAY`.

    Base64 cryptographic nonce provided by the device's wallet.
    """
