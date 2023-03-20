# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountHolderUpdateResponse"]


class AccountHolderUpdateResponse(BaseModel):
    business_account_token: Optional[str]
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll businesses
    with authorized users. Pass the account_token of the enrolled business
    associated with the AUTHORIZED_USER in this field.
    """

    email: Optional[str]
    """The newly updated email for the account holder"""

    phone_number: Optional[str]
    """The newly updated phone_number for the account holder"""

    token: Optional[str]
    """The token for the account holder that was updated"""
