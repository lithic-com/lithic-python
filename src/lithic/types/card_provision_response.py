# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .provision_response import ProvisionResponse

__all__ = ["CardProvisionResponse", "ProvisioningPayload"]

ProvisioningPayload: TypeAlias = Union[str, ProvisionResponse]


class CardProvisionResponse(BaseModel):
    provisioning_payload: Optional[ProvisioningPayload] = None
    """
    Base64 encoded JSON payload representing a payment card that can be passed to a
    device's digital wallet. Applies to Google and Samsung Pay wallets.
    """
