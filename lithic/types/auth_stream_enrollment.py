# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthStreamEnrollment"]


class AuthStreamEnrollment(BaseModel):
    enrolled: Optional[bool]
    """Whether ASA is enrolled."""
