# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["MicroDepositCreateParams"]


class MicroDepositCreateParams(TypedDict, total=False):
    micro_deposits: Required[List[int]]
