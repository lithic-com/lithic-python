# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["CardProductCreditDetailResponse"]


class CardProductCreditDetailResponse(BaseModel):
    credit_extended: int
    """The amount of credit extended within the program"""

    credit_limit: int
    """The total credit limit of the program"""
