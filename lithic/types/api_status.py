# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Any
from typing_extensions import Literal
from .._models import StringModel, NoneModel, BaseModel


__all__ = ["APIStatus"]


class APIStatus(BaseModel):
    message: Optional[str]
