# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardReassignAccountParams"]


class CardReassignAccountParams(TypedDict, total=False):
    new_account_token: Required[str]
    """Globally unique identifier for the account to associate with the card"""
