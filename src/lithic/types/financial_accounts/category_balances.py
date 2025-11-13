# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CategoryBalances"]


class CategoryBalances(BaseModel):
    fees: int

    interest: int

    principal: int
