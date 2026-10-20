# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["IPRangeRetrieveResponse"]


class IPRangeRetrieveResponse(BaseModel):
    responders: List[str]
    """IP ranges that responder requests are sent from, in CIDR notation"""

    updated: datetime
    """Date and time the IP ranges were last changed"""
