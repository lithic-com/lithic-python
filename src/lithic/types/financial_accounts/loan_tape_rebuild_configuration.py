# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["LoanTapeRebuildConfiguration"]


class LoanTapeRebuildConfiguration(BaseModel):
    """Configuration for building loan tapes"""

    rebuild_needed: bool
    """Whether the account's loan tapes need to be rebuilt or not"""

    last_rebuild: Optional[date] = None
    """The date for which the account's loan tapes were last rebuilt"""

    rebuild_from: Optional[date] = None
    """Date from which to start rebuilding from if the account requires a rebuild"""
