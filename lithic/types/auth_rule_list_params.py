# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional

from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

__all__ = ["AuthRuleListParams"]


class AuthRuleListParams(TypedDict, total=False):
    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""
