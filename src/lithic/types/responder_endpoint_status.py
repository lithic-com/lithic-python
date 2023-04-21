# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["ResponderEndpointStatus"]


class ResponderEndpointStatus(BaseModel):
    enrolled: Optional[bool]
    """True if the instance has an endpoint enrolled."""

    url: Optional[str]
    """The URL of the currently enrolled endpoint or null."""
