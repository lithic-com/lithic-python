# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..types import funding_source
from .._models import BaseModel

__all__ = ["FundingSourceListResponse"]


class FundingSourceListResponse(BaseModel):
    data: List[funding_source.FundingSource]

    page: int
    """Page number. Will always be 1."""

    total_entries: int
    """Total number of entries."""

    total_pages: int
    """Total number of pages. Will always be 1."""
