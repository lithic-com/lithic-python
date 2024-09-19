# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TokenizationResendActivationCodeParams"]


class TokenizationResendActivationCodeParams(TypedDict, total=False):
    activation_method_type: Literal["EMAIL_TO_CARDHOLDER_ADDRESS", "TEXT_TO_CARDHOLDER_NUMBER"]
    """
    The communication method that the user has selected to use to receive the
    authentication code. Supported Values: Sms = "TEXT_TO_CARDHOLDER_NUMBER". Email
    = "EMAIL_TO_CARDHOLDER_ADDRESS"
    """
