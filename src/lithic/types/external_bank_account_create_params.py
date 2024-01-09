# File generated from our OpenAPI spec by Stainless.

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

    country: Required[str]

    currency: Required[str]

    owner: Required[str]

    owner_type: Required[OwnerType]

    routing_number: Required[str]

    type: Required[Literal["CHECKING", "SAVINGS"]]

    verification_method: Required[VerificationMethod]

    account_token: str

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

    user_defined_id: str

    verification_enforcement: bool
    """Indicates whether verification was enforced for a given association record.

    For MICRO_DEPOSIT, option to disable verification if the external bank account
    has already been verified before. By default, verification will be required
    unless users pass in a value of false
    """


class PlaidCreateBankAccountAPIRequest(TypedDict, total=False):
    owner: Required[str]

    owner_type: Required[OwnerType]

    processor_token: Required[str]

    verification_method: Required[VerificationMethod]

    account_token: str

    company_id: str

    dob: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date of Birth of the Individual that owns the external bank account"""

    doing_business_as: str

    user_defined_id: str


ExternalBankAccountAddress = ExternalBankAccountAddressParam
"""This type is deprecated, please use ExternalBankAccountAddressParam instead"""

ExternalBankAccountCreateParams = Union[BankVerifiedCreateBankAccountAPIRequest, PlaidCreateBankAccountAPIRequest]
