# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExternalBankAccountAddress"]


class ExternalBankAccountAddress(BaseModel):
    address1: str

    city: str

    country: str

    postal_code: str

    state: str

    address2: Optional[str] = None
