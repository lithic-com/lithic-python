# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TokenizationSelectTfaMethodResponse"]


class TokenizationSelectTfaMethodResponse(BaseModel):
    success: bool
    """Whether the card network accepted the authentication method selection"""
