# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TokenizationSubmitTfaResponse"]


class TokenizationSubmitTfaResponse(BaseModel):
    success: bool
    """Whether the card network accepted the authentication code.

    A true value does not mean the tokenization is already active
    """
