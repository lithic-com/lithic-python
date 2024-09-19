# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V2ReportResponse"]


class V2ReportResponse(BaseModel):
    report_token: Optional[str] = None
