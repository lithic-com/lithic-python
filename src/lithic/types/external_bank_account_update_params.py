# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExternalBankAccountUpdateParams", "ExternalBankAccountAddress"]


class ExternalBankAccountUpdateParams(TypedDict, total=False):
    address: ExternalBankAccountAddress
    """
    Address used during Address Verification Service (AVS) checks during
    transactions if enabled via Auth Rules.
    """

    company_id: str

    dob: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date of Birth of the Individual that owns the external bank account"""

    doing_business_as: str

    name: str

    owner: str

    owner_type: Literal["INDIVIDUAL", "BUSINESS"]


class ExternalBankAccountAddress(TypedDict, total=False):
    address1: Required[str]

    city: Required[str]

    country: Required[str]

    postal_code: Required[str]

    state: Required[str]

    address2: str
