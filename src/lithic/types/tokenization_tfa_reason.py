# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TokenizationTfaReason"]

TokenizationTfaReason: TypeAlias = Literal[
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
