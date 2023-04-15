# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = ["KYCExempt"]


class KYCExempt(BaseModel):
    email: str
    """The KYC Exempt user's email"""

    first_name: str
    """The KYC Exempt user's first name"""

    kyc_exemption_type: Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"]
    """Specifies the type of KYC Exempt user"""

    last_name: str
    """The KYC Exempt user's last name"""

    phone_number: str
    """The KYC Exempt user's phone number"""

    workflow: Literal["KYC_EXEMPT"]
    """Specifies the workflow type. This must be 'KYC_EXEMPT'"""

    address: Optional[shared.Address]
    """
    KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    business_account_token: Optional[str]
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Pass the account_token of the enrolled business associated
    with the AUTHORIZED_USER in this field.
    """
