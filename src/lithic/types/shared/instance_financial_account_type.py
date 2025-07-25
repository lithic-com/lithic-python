# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["InstanceFinancialAccountType"]

InstanceFinancialAccountType: TypeAlias = Literal[
    "ISSUING",
    "RESERVE",
    "OPERATING",
    "CHARGED_OFF_FEES",
    "CHARGED_OFF_INTEREST",
    "CHARGED_OFF_PRINCIPAL",
    "SECURITY",
    "PROGRAM_RECEIVABLES",
    "COLLECTION",
]
