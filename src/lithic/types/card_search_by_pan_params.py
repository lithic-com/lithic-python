# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardSearchByPanParams"]


class CardSearchByPanParams(TypedDict, total=False):
    pan: Required[str]
    """The PAN for the card being retrieved."""
