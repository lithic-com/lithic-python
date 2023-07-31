# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..types import external_bank_account_address
from .._models import BaseModel

__all__ = ["ExternalBankAccountCreateResponse"]


class ExternalBankAccountCreateResponse(BaseModel):
    token: str
    """
    A globally unique identifier for this record of an external bank account
    association. If a program links an external bank account to more than one
    end-user or to both the program and the end-user, then Lithic will return each
    record of the association
    """

    country: str
    """The country that the bank account is located in using ISO 3166-1.

    We will only accept USA bank accounts e.g., USA
    """

    created: datetime
    """
    An ISO 8601 string representing when this funding source was added to the Lithic
    account.
    """

    currency: str
    """currency of the external account 3-digit alphabetic ISO 4217 code"""

    last_four: str
    """The last 4 digits of the bank account.

    Derived by Lithic from the account number passed
    """

    owner: str
    """Legal Name of the business or individual who owns the external account.

    This will appear in statements
    """

    owner_type: Literal["INDIVIDUAL", "BUSINESS"]

    routing_number: str

    state: Literal["ENABLED", "CLOSED", "PAUSED"]

    type: Literal["CHECKING", "SAVINGS"]

    verification_method: Literal["MANUAL", "MICRO_DEPOSIT", "PLAID"]

    verification_state: Literal["PENDING", "ENABLED", "FAILED_VERIFICATION"]

    account_token: Optional[str]
    """Indicates which Lithic account the external account is associated with.

    For external accounts that are associated with the program, account_token field
    returned will be null
    """

    address: Optional[external_bank_account_address.ExternalBankAccountAddress]
    """
    Address used during Address Verification Service (AVS) checks during
    transactions if enabled via Auth Rules.
    """

    company_id: Optional[str]
    """Optional field that helps identify bank accounts in receipts"""

    dob: Optional[date]
    """Date of Birth of the Individual that owns the external bank account"""

    doing_business_as: Optional[str]

    name: Optional[str]
    """The nickname given to this record of External Bank Account"""
