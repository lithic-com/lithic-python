# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardWebProvisionParams"]


class CardWebProvisionParams(TypedDict, total=False):
    digital_wallet: Literal["APPLE_PAY"]
    """Name of digital wallet provider."""
