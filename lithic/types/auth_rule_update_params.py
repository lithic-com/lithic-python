# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AuthRuleUpdateParams"]


class AuthRuleUpdateParams(TypedDict, total=False):
    allowed_countries: List[str]
    """Array of country codes for which the Auth Rule will permit transactions.

    Note that only this field or `blocked_countries` can be used for a given Auth
    Rule.
    """

    allowed_mcc: List[str]
    """
    Array of merchant category codes for which the Auth Rule will permit
    transactions. Note that only this field or `blocked_mcc` can be used for a given
    Auth Rule.
    """

    avs_type: Literal["ZIP_ONLY"]
    """
    Address verification to confirm that postal code entered at point of transaction
    (if applicable) matches the postal code on file for a given card.
    """

    blocked_countries: List[str]
    """
    Array of country codes for which the Auth Rule will automatically decline
    transactions. Note that only this field or `allowed_countries` can be used for a
    given Auth Rule.
    """

    blocked_mcc: List[str]
    """
    Array of merchant category codes for which the Auth Rule will automatically
    decline transactions. Note that only this field or `allowed_mcc` can be used for
    a given Auth Rule.
    """
