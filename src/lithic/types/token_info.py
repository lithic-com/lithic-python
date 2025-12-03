# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TokenInfo"]


class TokenInfo(BaseModel):
    wallet_type: Literal["APPLE_PAY", "GOOGLE_PAY", "MASTERPASS", "MERCHANT", "OTHER", "SAMSUNG_PAY"]
    """The wallet_type field will indicate the source of the token.

    Possible token sources include digital wallets (Apple, Google, or Samsung Pay),
    merchant tokenization, and “other” sources like in-flight commerce. Masterpass
    is not currently supported and is included for future use.
    """
