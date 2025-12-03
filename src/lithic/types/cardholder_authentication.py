# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardholderAuthentication"]


class CardholderAuthentication(BaseModel):
    authentication_method: Literal["FRICTIONLESS", "CHALLENGE", "NONE"]
    """Indicates the method used to authenticate the cardholder."""

    authentication_result: Literal["ATTEMPTS", "DECLINE", "NONE", "SUCCESS"]
    """Indicates the outcome of the 3DS authentication process."""

    decision_made_by: Literal[
        "CUSTOMER_RULES", "CUSTOMER_ENDPOINT", "LITHIC_DEFAULT", "LITHIC_RULES", "NETWORK", "UNKNOWN"
    ]
    """Indicates which party made the 3DS authentication decision."""

    liability_shift: Literal["3DS_AUTHENTICATED", "TOKEN_AUTHENTICATED", "NONE"]
    """Indicates whether chargeback liability shift applies to the transaction.

    Possible enum values:

    - `3DS_AUTHENTICATED`: The transaction was fully authenticated through a 3-D
      Secure flow, chargeback liability shift applies.
    - `NONE`: Chargeback liability shift has not shifted to the issuer, i.e. the
      merchant is liable.
    - `TOKEN_AUTHENTICATED`: The transaction was a tokenized payment with validated
      cryptography, possibly recurring. Chargeback liability shift to the issuer
      applies.
    """

    three_ds_authentication_token: Optional[str] = None
    """
    Unique identifier you can use to match a given 3DS authentication (available via
    the three_ds_authentication.created event webhook) and the transaction. Note
    that in cases where liability shift does not occur, this token is matched to the
    transaction on a best-effort basis.
    """
