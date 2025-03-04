# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthenticationSimulateOtpEntryParams"]


class AuthenticationSimulateOtpEntryParams(TypedDict, total=False):
    token: Required[str]
    """
    A unique token returned as part of a /v1/three_ds_authentication/simulate call
    that resulted in PENDING_CHALLENGE authentication result.
    """

    otp: Required[str]
    """The OTP entered by the cardholder"""
