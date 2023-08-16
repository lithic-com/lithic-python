# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["APIStatus"]


class APIStatus(BaseModel):
    message: Optional[str] = None
