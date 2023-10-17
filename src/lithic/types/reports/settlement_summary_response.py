# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel
from ..settlement_report import SettlementReport

__all__ = ["SettlementSummaryResponse"]


class SettlementSummaryResponse(BaseModel):
    data: List[SettlementReport]
