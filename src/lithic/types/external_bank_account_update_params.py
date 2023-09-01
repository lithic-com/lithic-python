# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .owner_type import OwnerType
from .external_bank_account_address_param import ExternalBankAccountAddressParam

__all__ = ["ExternalBankAccountUpdateParams"]


class ExternalBankAccountUpdateParams(TypedDict, total=False):
    address: ExternalBankAccountAddressParam
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

    owner_type: OwnerType

    user_defined_id: str


ExternalBankAccountAddress = ExternalBankAccountAddressParam
"""This type is deprecated, please use ExternalBankAccountAddressParam instead"""
