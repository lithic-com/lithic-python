# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .owner_type import OwnerType
from .verification_method import VerificationMethod
from .external_bank_account_address_param import ExternalBankAccountAddressParam

__all__ = [
    "ExternalBankAccountCreateParams",
    "BankVerifiedCreateBankAccountAPIRequest",
    "PlaidCreateBankAccountAPIRequest",
]


class BankVerifiedCreateBankAccountAPIRequest(TypedDict, total=False):
    account_number: Required[str]
    """Routing Number"""

    country: Required[str]
    """The country that the bank account is located in using ISO 3166-1.

    We will only accept USA bank accounts e.g., USA
    """

    currency: Required[str]
    """currency of the external account 3-digit alphabetic ISO 4217 code"""

    owner: Required[str]
    """Legal Name of the business or individual who owns the external account.

    This will appear in statements
    """

    owner_type: Required[OwnerType]
    """Owner Type"""

    routing_number: Required[str]
    """Routing Number"""

    type: Required[Literal["CHECKING", "SAVINGS"]]
    """Account Type"""

    verification_method: Required[VerificationMethod]
    """Verification Method"""

    account_token: str
    """Indicates which Lithic account the external account is associated with.

    For external accounts that are associated with the program, account_token field
    returned will be null
    """

    address: ExternalBankAccountAddressParam
    """Address"""

    company_id: str
    """Optional field that helps identify bank accounts in receipts"""

    dob: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date of Birth of the Individual that owns the external bank account"""

    doing_business_as: str
    """Doing Business As"""

    financial_account_token: str
    """The financial account token of the operating account to fund the micro deposits"""

    name: str
    """The nickname given to this record of External Bank Account"""

    user_defined_id: str
    """User Defined ID"""

    verification_enforcement: bool


class PlaidCreateBankAccountAPIRequest(TypedDict, total=False):
    owner: Required[str]
    """Legal Name of the business or individual who owns the external account.

    This will appear in statements
    """

    owner_type: Required[OwnerType]
    """Owner Type"""

    processor_token: Required[str]

    verification_method: Required[VerificationMethod]
    """Verification Method"""

    account_token: str
    """Indicates which Lithic account the external account is associated with.

    For external accounts that are associated with the program, account_token field
    returned will be null
    """

    company_id: str
    """Optional field that helps identify bank accounts in receipts"""

    dob: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date of Birth of the Individual that owns the external bank account"""

    doing_business_as: str
    """Doing Business As"""

    user_defined_id: str
    """User Defined ID"""


ExternalBankAccountAddress = ExternalBankAccountAddressParam
"""This type is deprecated, please use ExternalBankAccountAddressParam instead"""

ExternalBankAccountCreateParams = Union[BankVerifiedCreateBankAccountAPIRequest, PlaidCreateBankAccountAPIRequest]
