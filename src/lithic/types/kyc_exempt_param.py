# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared_params.address import Address

__all__ = ["KYCExemptParam"]


class KYCExemptParam(TypedDict, total=False):
    address: Required[Address]
    """
    KYC Exempt user's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    email: Required[str]
    """The KYC Exempt user's email"""

    first_name: Required[str]
    """The KYC Exempt user's first name"""

    kyc_exemption_type: Required[Literal["AUTHORIZED_USER", "PREPAID_CARD_USER"]]
    """Specifies the type of KYC Exempt user"""

    last_name: Required[str]
    """The KYC Exempt user's last name"""

    phone_number: Required[str]
    """The KYC Exempt user's phone number, entered in E.164 format."""

    workflow: Required[Literal["KYC_EXEMPT"]]
    """Specifies the workflow type. This must be 'KYC_EXEMPT'"""

    business_account_token: str
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Pass the account_token of the enrolled business associated
    with the AUTHORIZED_USER in this field.
    """

    external_id: str
    """
    A user provided id that can be used to link an account holder with an external
    system
    """
