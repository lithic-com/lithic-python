# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .events.enhanced_data import EnhancedData

__all__ = ["EnhancedCommercialDataRetrieveResponse"]


class EnhancedCommercialDataRetrieveResponse(BaseModel):
    data: List[EnhancedData]
