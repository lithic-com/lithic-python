# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AuthRuleListParams"]


class AuthRuleListParams(TypedDict, total=False):
    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""
