# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ..statement import Statement

__all__ = ["Statements"]


class Statements(BaseModel):
    data: List[Statement]

    has_more: bool
