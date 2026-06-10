# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ResolutionOutcome"]

ResolutionOutcome: TypeAlias = Literal[
    "CONFIRMED_FRAUD", "SUSPICIOUS_ACTIVITY", "FALSE_POSITIVE", "NO_ACTION_REQUIRED", "ESCALATED_EXTERNAL"
]
