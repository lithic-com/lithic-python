# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .owner_type import OwnerType
from .external_bank_account_address_param import ExternalBankAccountAddressParam

__all__ = ["ExternalBankAccountUpdateParams"]


class ExternalBankAccountUpdateParams(TypedDict, total=False):
    address: ExternalBankAccountAddressParam
    """Address"""

    company_id: str
    """Optional field that helps identify bank accounts in receipts"""

    dob: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date of Birth of the Individual that owns the external bank account"""

    doing_business_as: str
    """Doing Business As"""

    name: str
    """The nickname for this External Bank Account"""

    owner: str
    """Legal Name of the business or individual who owns the external account.

    This will appear in statements
    """

    owner_type: OwnerType
    """Owner Type"""

    type: Literal["CHECKING", "SAVINGS"]

    user_defined_id: str
    """User Defined ID"""


ExternalBankAccountAddress = ExternalBankAccountAddressParam
"""This type is deprecated, please use ExternalBankAccountAddressParam instead"""
