# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ConditionalAttribute"]

ConditionalAttribute: TypeAlias = Literal[
    "MCC",
    "COUNTRY",
    "CURRENCY",
    "MERCHANT_ID",
    "DESCRIPTOR",
    "LIABILITY_SHIFT",
    "PAN_ENTRY_MODE",
    "TRANSACTION_AMOUNT",
    "RISK_SCORE",
    "CARD_TRANSACTION_COUNT_1H",
    "CARD_TRANSACTION_COUNT_24H",
    "CARD_STATE",
]
