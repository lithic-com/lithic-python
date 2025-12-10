# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Device"]


class Device(BaseModel):
    imei: Optional[str] = None
    """The IMEI number of the device being provisioned.

    For Amex, this field contains device ID instead as IMEI is not provided
    """

    ip_address: Optional[str] = None
    """The IP address of the device initiating the request"""

    location: Optional[str] = None
    """
    Latitude and longitude where the device is located during the authorization
    attempt
    """
