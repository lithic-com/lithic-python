# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountHolderUpdateParams"]


class AccountHolderUpdateParams(TypedDict, total=False):
    business_account_token: str
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Pass the account_token of the enrolled business associated
    with the AUTHORIZED_USER in this field.
    """

    email: str
    """Account holder's email address.

    The primary purpose of this field is for cardholder identification and
    verification during the digital wallet tokenization process.
    """

    phone_number: str
    """Account holder's phone number, entered in E.164 format.

    The primary purpose of this field is for cardholder identification and
    verification during the digital wallet tokenization process.
    """
