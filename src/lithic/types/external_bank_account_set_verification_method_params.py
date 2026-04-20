# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalBankAccountSetVerificationMethodParams"]


class ExternalBankAccountSetVerificationMethodParams(TypedDict, total=False):
    verification_method: Required[Literal["MICRO_DEPOSIT", "PRENOTE", "EXTERNALLY_VERIFIED"]]
    """The verification method to set for the external bank account"""

    financial_account_token: str
    """The financial account token of the operating account to fund the micro deposits.

    Required when verification_method is MICRO_DEPOSIT or PRENOTE.
    """
