# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountHolderUpdateResponse"]


class AccountHolderUpdateResponse(BaseModel):
    token: Optional[str] = None
    """The token for the account holder that was updated"""

    business_account_token: Optional[str] = None
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll businesses
    with authorized users. Pass the account_token of the enrolled business
    associated with the AUTHORIZED_USER in this field.
    """

    email: Optional[str] = None
    """The newly updated email for the account holder"""

    phone_number: Optional[str] = None
    """The newly updated phone_number for the account holder"""
