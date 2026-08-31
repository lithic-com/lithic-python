# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .owner_type import OwnerType

__all__ = ["BlockchainRecipientCreateParams"]


class BlockchainRecipientCreateParams(TypedDict, total=False):
    account_token: Required[str]
    """The financial account the blockchain recipient belongs to"""

    address: Required[str]
    """The blockchain address funds will be withdrawn to"""

    chain: Required[str]
    """The blockchain network that the address belongs to"""

    owner: Required[str]
    """Legal name of the business or individual who owns the blockchain address"""

    owner_type: Required[OwnerType]
    """Owner Type"""

    address_tag: str
    """
    An optional tag or memo used by some chains to identify the destination of a
    transfer within a shared address
    """

    name: str
    """The nickname for this blockchain recipient"""
