# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .external_resource_type import ExternalResourceType

__all__ = ["ExternalResource"]


class ExternalResource(BaseModel):
    external_resource_token: str
    """Token identifying the external resource"""

    external_resource_type: ExternalResourceType
    """Type of external resource associated with the management operation"""

    external_resource_sub_token: Optional[str] = None
    """Token identifying the external resource sub-resource"""
