# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["NetworkProgram"]


class NetworkProgram(BaseModel):
    token: str
    """Lithic-generated unique identifier for the program"""

    default_product_code: str
    """Network product ID associated with this program."""

    name: str
    """The name of the network program."""

    registered_program_identification_number: str
    """RPIN value assigned by the network."""
