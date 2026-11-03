# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TokenizationCreatePaymentCredentialsParams", "Device", "Mandate", "MandateMerchant"]


class TokenizationCreatePaymentCredentialsParams(TypedDict, total=False):
    device: Required[Device]
    """Device used for the purchase"""

    mandate: Required[Mandate]

    type: Required[Literal["AUTONOMOUS", "HUMAN_IN_THE_LOOP", "RECURRING"]]
    """Type of purchase for which payment credentials are requested"""


class Device(TypedDict, total=False):
    """Device used for the purchase"""

    application_name: Required[str]
    """Name of the application used for the purchase"""

    brand: Required[str]
    """Device brand"""

    ip_address: Required[str]
    """IP address of the device"""

    type: Required[str]
    """Device type"""


class MandateMerchant(TypedDict, total=False):
    name: Required[str]
    """Merchant name"""

    url: Required[str]
    """Merchant website URL"""


class Mandate(TypedDict, total=False):
    amount: Required[int]
    """Purchase amount and mandate limit in USD cents"""

    expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    Date and time when the mandate expires, independent of the payment credentials'
    expiration
    """

    frequency: Required[Literal["ONE_TIME", "WEEKLY", "MONTHLY", "YEARLY"]]
    """Purchase frequency. RECURRING purchases require WEEKLY, MONTHLY, or YEARLY"""

    merchant: Required[MandateMerchant]
