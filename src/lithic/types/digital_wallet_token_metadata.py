# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalWalletTokenMetadata", "PaymentAccountInfo", "PaymentAccountInfoAccountHolderData"]


class PaymentAccountInfoAccountHolderData(BaseModel):
    """
    Additional information that can be used to identify the account holder, such as name, address, etc
    """

    phone_number: Optional[str] = None
    """
    The phone number, may contain country code along with phone number when
    countryDialInCode is not present
    """


class PaymentAccountInfo(BaseModel):
    """Contains the information of the account responsible for the payment."""

    account_holder_data: PaymentAccountInfoAccountHolderData
    """
    Additional information that can be used to identify the account holder, such as
    name, address, etc
    """

    pan_unique_reference: Optional[str] = None
    """Reference to the PAN that is unique per Wallet Provider"""

    payment_account_reference: Optional[str] = None
    """The unique account reference assigned to the PAN"""

    token_unique_reference: Optional[str] = None
    """
    A unique reference assigned following the allocation of a token used to identify
    the token for the duration of its lifetime.
    """


class DigitalWalletTokenMetadata(BaseModel):
    """Contains the metadata for the digital wallet being tokenized."""

    payment_account_info: PaymentAccountInfo
    """Contains the information of the account responsible for the payment."""

    status: str
    """The current status of the digital wallet token. Pending or declined."""

    payment_app_instance_id: Optional[str] = None
    """
    The identifier of the Payment App instance within a device that will be
    provisioned with a token
    """

    token_requestor_id: Optional[str] = None
    """The party that requested the digitization"""

    token_requestor_name: Optional[
        Literal[
            "AMAZON_ONE",
            "ANDROID_PAY",
            "APPLE_PAY",
            "FACEBOOK",
            "FITBIT_PAY",
            "GARMIN_PAY",
            "MICROSOFT_PAY",
            "NETFLIX",
            "SAMSUNG_PAY",
            "UNKNOWN",
            "VISA_CHECKOUT",
        ]
    ] = None
    """Human-readable name of the wallet that the token_requestor_id maps to."""
