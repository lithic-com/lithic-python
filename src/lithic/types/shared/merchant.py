# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Merchant"]


class Merchant(BaseModel):
    acceptor_id: str
    """Unique alphanumeric identifier for the payment card acceptor (merchant)."""

    acquiring_institution_id: str
    """Unique numeric identifier of the acquiring institution."""

    city: str
    """City of card acceptor.

    Note that in many cases, particularly in card-not-present transactions,
    merchants may send through a phone number or URL in this field.
    """

    country: str
    """Country or entity of card acceptor.

    Possible values are: (1) all ISO 3166-1 alpha-3 country codes, (2) QZZ for
    Kosovo, and (3) ANT for Netherlands Antilles.
    """

    descriptor: str
    """Short description of card acceptor."""

    mcc: str
    """Merchant category code (MCC).

    A four-digit number listed in ISO 18245. An MCC is used to classify a business
    by the types of goods or services it provides.
    """

    state: str
    """Geographic state of card acceptor."""
