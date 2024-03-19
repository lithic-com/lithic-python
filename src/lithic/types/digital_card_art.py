# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DigitalCardArt"]


class DigitalCardArt(BaseModel):
    token: str
    """Globally unique identifier for the card art."""

    card_program_token: str
    """Globally unique identifier for the card program."""

    created: datetime
    """Timestamp of when card art was created."""

    description: str
    """Description of the card art."""

    is_enabled: bool
    """Whether the card art is enabled."""

    network: Literal["MASTERCARD", "VISA"]
    """Card network."""

    is_card_program_default: Optional[bool] = None
    """Whether the card art is the default card art to be added upon tokenization."""
