# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

from .velocity_limit_filters_param import VelocityLimitFiltersParam

__all__ = ["SpendVelocityFiltersParam"]


class SpendVelocityFiltersParam(VelocityLimitFiltersParam, total=False):
    exclude_tags: Optional[Dict[str, str]]
    """Tag key-value pairs to exclude from the velocity calculation.

    Transactions matching all specified tag key-value pairs will be excluded from
    the calculated velocity.
    """

    include_tags: Optional[Dict[str, str]]
    """Tag key-value pairs to include in the velocity calculation.

    Only transactions matching all specified tag key-value pairs will be included in
    the calculated velocity.
    """
