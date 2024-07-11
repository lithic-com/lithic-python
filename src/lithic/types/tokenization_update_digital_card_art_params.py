# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TokenizationUpdateDigitalCardArtParams"]


class TokenizationUpdateDigitalCardArtParams(TypedDict, total=False):
    digital_card_art_token: str
    """
    Specifies the digital card art to be displayed in the user’s digital wallet for
    a tokenization. This artwork must be approved by the network and configured by
    Lithic to use. See
    [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).
    """
