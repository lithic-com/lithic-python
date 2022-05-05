# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Any
from typing_extensions import Literal
from .._models import StringModel, NoneModel, BaseModel
from ..types import funding_source


__all__ = ["CardProvisionResponse"]


class CardProvisionResponse(BaseModel):
    provisioning_payload: Optional[str]
