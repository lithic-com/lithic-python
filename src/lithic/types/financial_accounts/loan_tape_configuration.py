# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .loan_tape_rebuild_configuration import LoanTapeRebuildConfiguration

__all__ = ["LoanTapeConfiguration"]


class LoanTapeConfiguration(BaseModel):
    """Configuration for loan tapes"""

    created_at: datetime

    financial_account_token: str

    instance_token: str

    updated_at: datetime

    credit_product_token: Optional[str] = None

    loan_tape_rebuild_configuration: Optional[LoanTapeRebuildConfiguration] = None
    """Configuration for building loan tapes"""

    tier_schedule_changed_at: Optional[datetime] = None
