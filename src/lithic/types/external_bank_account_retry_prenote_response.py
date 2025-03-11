# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .owner_type import OwnerType
from .verification_method import VerificationMethod
from .external_bank_account_address import ExternalBankAccountAddress

__all__ = ["ExternalBankAccountRetryPrenoteResponse"]


class ExternalBankAccountRetryPrenoteResponse(BaseModel):
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
    """currency of the external account 3-character alphabetic ISO 4217 code"""

    last_four: str
    """The last 4 digits of the bank account.

    Derived by Lithic from the account number passed
    """

    owner: str
    """Legal Name of the business or individual who owns the external account.

    This will appear in statements
    """

    owner_type: OwnerType
    """Owner Type"""

    routing_number: str
    """Routing Number"""

    state: Literal["ENABLED", "CLOSED", "PAUSED"]
    """Account State"""

    type: Literal["CHECKING", "SAVINGS"]
    """Account Type"""

    verification_attempts: int
    """The number of attempts at verification"""

    verification_method: VerificationMethod
    """Verification Method"""

    verification_state: Literal["PENDING", "ENABLED", "FAILED_VERIFICATION", "INSUFFICIENT_FUNDS"]
    """Verification State"""

    account_token: Optional[str] = None
    """Indicates which Lithic account the external account is associated with.

    For external accounts that are associated with the program, account_token field
    returned will be null
    """

    address: Optional[ExternalBankAccountAddress] = None
    """Address"""

    company_id: Optional[str] = None
    """Optional field that helps identify bank accounts in receipts"""

    dob: Optional[date] = None
    """Date of Birth of the Individual that owns the external bank account"""

    doing_business_as: Optional[str] = None
    """Doing Business As"""

    financial_account_token: Optional[str] = None
    """The financial account token of the operating account to fund the micro deposits"""

    name: Optional[str] = None
    """The nickname for this External Bank Account"""

    user_defined_id: Optional[str] = None
    """User Defined ID"""

    verification_failed_reason: Optional[str] = None
    """Optional free text description of the reason for the failed verification.

    For ACH micro-deposits returned, this field will display the reason return code
    sent by the ACH network
    """
