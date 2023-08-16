# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["CardProvisionResponse"]


class CardProvisionResponse(BaseModel):
    provisioning_payload: Optional[str] = None
