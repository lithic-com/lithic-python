# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardProvisionParams"]


class CardProvisionParams(TypedDict, total=False):
    certificate: str
    """Only applicable if `digital_wallet` is `APPLE_PAY`.

    Omit to receive only `activationData` in the response. Apple's public leaf
    certificate. Base64 encoded in PEM format with headers
    `(-----BEGIN CERTIFICATE-----)` and trailers omitted. Provided by the device's
    wallet.
    """

    digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"]
    """Name of digital wallet provider."""

    nonce: str
    """Only applicable if `digital_wallet` is `APPLE_PAY`.

    Omit to receive only `activationData` in the response. Base64 cryptographic
    nonce provided by the device's wallet.
    """

    nonce_signature: str
    """Only applicable if `digital_wallet` is `APPLE_PAY`.

    Omit to receive only `activationData` in the response. Base64 cryptographic
    nonce provided by the device's wallet.
    """
