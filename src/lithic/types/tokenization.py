# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tokenization", "Event", "EventRuleResult"]


class EventRuleResult(BaseModel):
    auth_rule_token: Optional[str] = None
    """The Auth Rule Token associated with the rule.

    If this is set to null, then the result was not associated with a
    customer-configured rule. This may happen in cases where a tokenization is
    declined or requires TFA due to a Lithic-configured security or compliance rule,
    for example.
    """

    explanation: Optional[str] = None
    """A human-readable explanation outlining the motivation for the rule's result"""

    name: Optional[str] = None
    """The name for the rule, if any was configured"""

    result: Literal["APPROVED", "DECLINED", "REQUIRE_TFA", "ERROR"]
    """The result associated with this rule"""


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
            "TOKEN_DELETED_FROM_CONSUMER_APP",
            "TOKEN_INACTIVE",
            "TOKEN_STATE_UNKNOWN",
            "TOKEN_SUSPENDED",
            "TOKEN_UPDATED",
        ]
    ] = None
    """Enum representing the result of the tokenization event"""

    rule_results: Optional[List[EventRuleResult]] = None
    """Results from rules that were evaluated for this tokenization"""

    tokenization_decline_reasons: Optional[
        List[
            Literal[
                "ACCOUNT_SCORE_1",
                "DEVICE_SCORE_1",
                "ALL_WALLET_DECLINE_REASONS_PRESENT",
                "WALLET_RECOMMENDED_DECISION_RED",
                "CVC_MISMATCH",
                "CARD_EXPIRY_MONTH_MISMATCH",
                "CARD_EXPIRY_YEAR_MISMATCH",
                "CARD_INVALID_STATE",
                "CUSTOMER_RED_PATH",
                "INVALID_CUSTOMER_RESPONSE",
                "NETWORK_FAILURE",
                "GENERIC_DECLINE",
                "DIGITAL_CARD_ART_REQUIRED",
            ]
        ]
    ] = None
    """List of reasons why the tokenization was declined"""

    tokenization_tfa_reasons: Optional[
        List[
            Literal[
                "WALLET_RECOMMENDED_TFA",
                "SUSPICIOUS_ACTIVITY",
                "DEVICE_RECENTLY_LOST",
                "TOO_MANY_RECENT_ATTEMPTS",
                "TOO_MANY_RECENT_TOKENS",
                "TOO_MANY_DIFFERENT_CARDHOLDERS",
                "OUTSIDE_HOME_TERRITORY",
                "HAS_SUSPENDED_TOKENS",
                "HIGH_RISK",
                "ACCOUNT_SCORE_LOW",
                "DEVICE_SCORE_LOW",
                "CARD_STATE_TFA",
                "HARDCODED_TFA",
                "CUSTOMER_RULE_TFA",
                "DEVICE_HOST_CARD_EMULATION",
            ]
        ]
    ] = None
    """List of reasons why two-factor authentication was required"""

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

    token_requestor_name: Union[
        Literal[
            "AMAZON_ONE",
            "ANDROID_PAY",
            "APPLE_PAY",
            "FACEBOOK",
            "FITBIT_PAY",
            "GARMIN_PAY",
            "GOOGLE_PAY",
            "MICROSOFT_PAY",
            "NETFLIX",
            "SAMSUNG_PAY",
            "UNKNOWN",
            "VISA_CHECKOUT",
        ],
        str,
    ]
    """The entity that requested the tokenization.

    For digital wallets, this will be one of the defined wallet types. For merchant
    tokenizations, this will be a free-form merchant name string.
    """

    token_unique_reference: str
    """The network's unique reference for the tokenization."""

    tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT"]
    """The channel through which the tokenization was made."""

    updated_at: datetime
    """Latest date and time when the tokenization was updated. UTC time zone."""

    device_id: Optional[str] = None
    """The device identifier associated with the tokenization."""

    digital_card_art_token: Optional[str] = None
    """
    Specifies the digital card art displayed in the user's digital wallet after
    tokenization. This will be null if the tokenization was created without an
    associated digital card art. See
    [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).
    """

    events: Optional[List[Event]] = None
    """A list of events related to the tokenization."""

    payment_account_reference_id: Optional[str] = None
    """The network's unique reference for the card that is tokenized."""
