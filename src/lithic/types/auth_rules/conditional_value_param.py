# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypeAlias

from ..._types import SequenceNotStr

__all__ = ["ConditionalValueParam"]

ConditionalValueParam: TypeAlias = Union[str, int, SequenceNotStr[str], Union[str, datetime]]
