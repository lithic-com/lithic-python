# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TokenizationDeclineReason"]

TokenizationDeclineReason: TypeAlias = Literal[
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
