# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TokenizationCreatePaymentCredentialsResponse", "Credentials", "Mandate", "MandateMerchant"]


class Credentials(BaseModel):
    """Payment credential and dynamic security code for the purchase"""

    cvv: str
    """Dynamic card security code for the purchase"""

    expiration_month: str
    """Expiration month of the payment credential"""

    expiration_year: str
    """Expiration year of the payment credential"""

    expires_at: datetime
    """Date and time when the dynamic security code expires"""

    value: str
    """Payment credential to use as the card number for the purchase"""


class MandateMerchant(BaseModel):
    name: str
    """Merchant name"""

    url: str
    """Merchant website URL"""


class Mandate(BaseModel):
    token: str
    """Globally unique identifier for the mandate"""

    amount: int
    """Purchase amount and mandate limit in USD cents"""

    expires_at: datetime
    """
    Date and time when the mandate expires, independent of the payment credentials'
    expiration
    """

    frequency: Literal["ONE_TIME", "WEEKLY", "MONTHLY", "YEARLY"]
    """Purchase frequency. RECURRING purchases require WEEKLY, MONTHLY, or YEARLY"""

    merchant: MandateMerchant

    status: Literal["PENDING", "COMPLETED", "CANCELLED"]
    """Status of the mandate. New mandates have status PENDING"""


class TokenizationCreatePaymentCredentialsResponse(BaseModel):
    token: str
    """Globally unique identifier for the payment credential resource"""

    agent_token: str
    """Globally unique identifier for the associated agent"""

    created_at: datetime
    """Date and time when the payment credential resource was created"""

    credentials: Credentials
    """Payment credential and dynamic security code for the purchase"""

    mandate: Mandate

    status: Literal["ACTIVE", "DEACTIVATED", "COMPLETED", "CANCELLED"]
    """Status of the payment credential resource. New credentials have status ACTIVE"""

    tokenization_token: str
    """Globally unique identifier for the associated tokenization"""

    type: Literal["AUTONOMOUS", "HUMAN_IN_THE_LOOP", "RECURRING"]
    """Type of purchase for which payment credentials are requested"""

    updated_at: datetime
    """Date and time when the payment credential resource was last updated"""
