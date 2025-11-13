# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CategoryDetails"]


class CategoryDetails(BaseModel):
    balance_transfers: str

    cash_advances: str

    purchases: str
