# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentReturnParams"]


class PaymentReturnParams(TypedDict, total=False):
    financial_account_token: Required[str]
    """Globally unique identifier for the financial account"""

    return_reason_code: Required[str]
    """ACH return reason code indicating the reason for returning the payment.

    Supported codes include R01-R53 and R80-R85. For a complete list of return codes
    and their meanings, see
    [ACH Return Reasons](https://docs.lithic.com/docs/ach-overview#ach-return-reasons)
    """

    addenda: Optional[str]
    """Optional additional information about the return. Limited to 44 characters"""

    date_of_death: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Date of death in YYYY-MM-DD format.

    Required when using return codes **R14** (representative payee deceased) or
    **R15** (beneficiary or account holder deceased)
    """

    memo: Optional[str]
    """Optional memo for the return. Limited to 10 characters"""
