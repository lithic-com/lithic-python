# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ConditionalOperation"]

ConditionalOperation: TypeAlias = Literal[
    "IS_ONE_OF",
    "IS_NOT_ONE_OF",
    "MATCHES",
    "DOES_NOT_MATCH",
    "IS_EQUAL_TO",
    "IS_NOT_EQUAL_TO",
    "IS_GREATER_THAN",
    "IS_GREATER_THAN_OR_EQUAL_TO",
    "IS_LESS_THAN",
    "IS_LESS_THAN_OR_EQUAL_TO",
    "IS_AFTER",
    "IS_BEFORE",
    "CONTAINS_ANY",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
]
