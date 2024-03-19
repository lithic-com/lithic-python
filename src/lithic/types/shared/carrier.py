# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Carrier"]


class Carrier(BaseModel):
    qr_code_url: Optional[str] = None
    """QR code url to display on the card carrier"""
