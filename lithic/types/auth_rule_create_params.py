# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["AuthRuleCreateParams"]


class AuthRuleCreateParams(TypedDict, total=False):
    account_tokens: List[str]
    """Array of account_token(s) identifying the accounts that the Auth Rule applies to. Note that only this field or `card_tokens` can be provided for a given Auth Rule."""

    allowed_countries: List[str]
    """Array of country codes for which the Auth Rule will permit transactions. Note that only this field or `blocked_countries` can be used for a given Auth Rule."""

    allowed_mcc: List[str]
    """Array of merchant category codes for which the Auth Rule will permit transactions. Note that only this field or `blocked_mcc` can be used for a given Auth Rule."""

    avs_type: Literal["ZIP_ONLY"]
    """Address verification to confirm that postal code entered at point of transaction (if applicable) matches the postal code on file for a given card."""

    blocked_countries: List[str]
    """Array of country codes for which the Auth Rule will automatically decline transactions. Note that only this field or `allowed_countries` can be used for a given Auth Rule."""

    blocked_mcc: List[str]
    """Array of merchant category codes for which the Auth Rule will automatically decline transactions. Note that only this field or `allowed_mcc` can be used for a given Auth Rule."""

    card_tokens: List[str]
    """Array of card_token(s) identifying the cards that the Auth Rule applies to. Note that only this field or `account_tokens` can be provided for a given Auth Rule."""

    program_level: bool
    """Boolean indicating whether the Auth Rule is applied at the program level."""
