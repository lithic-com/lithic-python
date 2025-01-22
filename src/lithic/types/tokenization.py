# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tokenization", "Event"]


class Event(BaseModel):
    token: Optional[str] = None
    """Globally unique identifier for a Tokenization Event"""

    created_at: Optional[datetime] = None
    """Date and time when the tokenization event first occurred. UTC time zone."""

    result: Optional[
        Literal[
            "APPROVED",
            "DECLINED",
            "NOTIFICATION_DELIVERED",
            "REQUIRE_ADDITIONAL_AUTHENTICATION",
            "TOKEN_ACTIVATED",
            "TOKEN_CREATED",
            "TOKEN_DEACTIVATED",
            "TOKEN_INACTIVE",
            "TOKEN_STATE_UNKNOWN",
            "TOKEN_SUSPENDED",
            "TOKEN_UPDATED",
        ]
    ] = None
    """Enum representing the result of the tokenization event"""

    type: Optional[
        Literal[
            "TOKENIZATION_2FA",
            "TOKENIZATION_AUTHORIZATION",
            "TOKENIZATION_DECISIONING",
            "TOKENIZATION_ELIGIBILITY_CHECK",
            "TOKENIZATION_UPDATED",
        ]
    ] = None
    """Enum representing the type of tokenization event that occurred"""


class Tokenization(BaseModel):
    token: str
    """Globally unique identifier for a Tokenization"""

    account_token: str
    """The account token associated with the card being tokenized."""

    card_token: str
    """The card token associated with the card being tokenized."""

    created_at: datetime
    """Date and time when the tokenization first occurred. UTC time zone."""

    status: Literal["ACTIVE", "DEACTIVATED", "INACTIVE", "PAUSED", "PENDING_2FA", "PENDING_ACTIVATION", "UNKNOWN"]
    """The status of the tokenization request"""

    token_requestor_name: Literal[
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
    """The entity that requested the tokenization.

    Represents a Digital Wallet or merchant.
    """

    token_unique_reference: str
    """The network's unique reference for the tokenization."""

    tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT"]
    """The channel through which the tokenization was made."""

    updated_at: datetime
    """Latest date and time when the tokenization was updated. UTC time zone."""

    digital_card_art_token: Optional[str] = None
    """
    Specifies the digital card art displayed in the user’s digital wallet after
    tokenization. This will be null if the tokenization was created without an
    associated digital card art. See
    [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).
    """

    events: Optional[List[Event]] = None
    """A list of events related to the tokenization."""

    payment_account_reference_id: Optional[str] = None
    """The network's unique reference for the card that is tokenized."""
