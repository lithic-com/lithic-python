# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["EventStream"]

EventStream: TypeAlias = Literal[
    "AUTHORIZATION", "THREE_DS_AUTHENTICATION", "TOKENIZATION", "ACH_CREDIT_RECEIPT", "ACH_DEBIT_RECEIPT"
]
