# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardWebProvisionParams"]


class CardWebProvisionParams(TypedDict, total=False):
    client_device_id: str
    """Only applicable if `digital_wallet` is GOOGLE_PAY.

    Google Pay Web Push Provisioning device identifier required for the tokenization
    flow
    """

    client_wallet_account_id: str
    """Only applicable if `digital_wallet` is GOOGLE_PAY.

    Google Pay Web Push Provisioning wallet account identifier required for the
    tokenization flow
    """

    digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY"]
    """Name of digital wallet provider."""

    server_session_id: str
    """Only applicable if `digital_wallet` is GOOGLE_PAY.

    Google Pay Web Push Provisioning session identifier required for the FPAN flow.
    """
