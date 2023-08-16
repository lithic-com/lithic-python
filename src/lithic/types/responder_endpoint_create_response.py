# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["ResponderEndpointCreateResponse"]


class ResponderEndpointCreateResponse(BaseModel):
    enrolled: Optional[bool] = None
    """True if the endpoint was enrolled successfully."""
