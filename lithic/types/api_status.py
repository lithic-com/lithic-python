# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from .._models import BaseModel, NoneModel, StringModel

__all__ = ["APIStatus"]


class APIStatus(BaseModel):
    message: Optional[str]
