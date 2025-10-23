# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProvisionResponse"]


class ProvisionResponse(BaseModel):
    activation_data: Optional[str] = FieldInfo(alias="activationData", default=None)

    encrypted_data: Optional[str] = FieldInfo(alias="encryptedData", default=None)

    ephemeral_public_key: Optional[str] = FieldInfo(alias="ephemeralPublicKey", default=None)
