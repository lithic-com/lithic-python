# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PaymentRetryParams"]


class PaymentRetryParams(TypedDict, total=False):
    method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"]
    """Settlement speed to retry the payment at.

    Defaults to the original payment's method. An `ACH_SAME_DAY` retry is rejected
    if the payment is for $1,000,000.00 or more, or if it is submitted after the
    same day ACH cutoff
    """
