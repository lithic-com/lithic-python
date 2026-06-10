# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CaseActivityType"]

CaseActivityType: TypeAlias = Literal[
    "STATUS", "TITLE", "ASSIGNED_TO", "RESOLUTION_OUTCOME", "RESOLUTION_NOTES", "TAGS", "PRIORITY", "COMMENT", "FILE"
]
