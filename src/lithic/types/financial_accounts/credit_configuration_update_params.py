# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CreditConfigurationUpdateParams", "AutoCollectionConfiguration"]


class CreditConfigurationUpdateParams(TypedDict, total=False):
    auto_collection_configuration: AutoCollectionConfiguration

    credit_limit: int

    credit_product_token: str
    """Globally unique identifier for the credit product.

    This can only be set while the financial account is in the `PENDING` state.
    Because assigning a credit product transitions the account to `OPEN`, a credit
    product can be attached only once; updating it on an account in any other state
    returns a `403`
    """

    external_bank_account_token: str

    tier: str
    """Tier to assign to a financial account"""


class AutoCollectionConfiguration(TypedDict, total=False):
    auto_collection_enabled: bool
    """If auto collection is enabled for this account"""
