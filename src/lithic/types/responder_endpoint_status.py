# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ResponderEndpointStatus"]


class ResponderEndpointStatus(BaseModel):
    enrolled: Optional[bool] = None
    """True if the instance has an endpoint enrolled."""

    url: Optional[str] = None
    """The URL of the currently enrolled endpoint or null."""
