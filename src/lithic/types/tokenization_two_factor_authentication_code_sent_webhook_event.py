# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TokenizationTwoFactorAuthenticationCodeSentWebhookEvent", "ActivationMethod"]


class ActivationMethod(BaseModel):
    type: Literal["EMAIL_TO_CARDHOLDER_ADDRESS", "TEXT_TO_CARDHOLDER_NUMBER"]
    """
    The communication method that the user has selected to use to receive the
    authentication code. Supported Values: Sms = "TEXT_TO_CARDHOLDER_NUMBER". Email
    = "EMAIL_TO_CARDHOLDER_ADDRESS"
    """

    value: str
    """
    The location to which the authentication code was sent. The format depends on
    the ActivationMethod.Type field. If Type is Email, the Value will be the email
    address. If the Type is Sms, the Value will be the phone number.
    """


class TokenizationTwoFactorAuthenticationCodeSentWebhookEvent(BaseModel):
    account_token: str
    """Unique identifier for the user tokenizing a card"""

    activation_method: ActivationMethod

    card_token: str
    """Unique identifier for the card being tokenized"""

    created: datetime
    """Indicate when the request was received from Mastercard or Visa"""

    event_type: Literal["tokenization.two_factor_authentication_code_sent"]
    """The type of event that occurred."""

    tokenization_token: str
    """Unique identifier for the tokenization"""
