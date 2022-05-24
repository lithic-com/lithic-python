# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from ..types import funding_source
from .._models import BaseModel, NoneModel, StringModel

__all__ = ["CardProvisionResponse"]


class CardProvisionResponse(BaseModel):
    provisioning_payload: Optional[str]
