# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "CardWebProvisionResponse",
    "AppleWebPushProvisioningResponse",
    "AppleWebPushProvisioningResponseJws",
    "AppleWebPushProvisioningResponseJwsHeader",
    "GoogleWebPushProvisioningResponse",
]


class AppleWebPushProvisioningResponseJwsHeader(BaseModel):
    """
    JWS unprotected headers containing header parameters that aren't integrity-protected by the JWS signature.
    """

    kid: Optional[str] = None
    """The ID for the JWS Public Key of the key pair used to generate the signature."""


class AppleWebPushProvisioningResponseJws(BaseModel):
    """JWS object required for handoff to Apple's script."""

    header: Optional[AppleWebPushProvisioningResponseJwsHeader] = None
    """
    JWS unprotected headers containing header parameters that aren't
    integrity-protected by the JWS signature.
    """

    payload: Optional[str] = None
    """Base64url encoded JSON object containing the provisioning payload."""

    protected: Optional[str] = None
    """
    Base64url encoded JWS protected headers containing the header parameters that
    are integrity-protected by the JWS signature.
    """

    signature: Optional[str] = None
    """Base64url encoded signature of the JWS object."""


class AppleWebPushProvisioningResponse(BaseModel):
    jws: Optional[AppleWebPushProvisioningResponseJws] = None
    """JWS object required for handoff to Apple's script."""

    state: Optional[str] = None
    """A unique identifier for the JWS object."""


class GoogleWebPushProvisioningResponse(BaseModel):
    google_opc: Optional[str] = None
    """
    A base64 encoded and encrypted payload representing card data for the Google Pay
    UWPP FPAN flow.
    """

    tsp_opc: Optional[str] = None
    """
    A base64 encoded and encrypted payload representing card data for the Google Pay
    UWPP tokenization flow.
    """


CardWebProvisionResponse: TypeAlias = Union[AppleWebPushProvisioningResponse, GoogleWebPushProvisioningResponse]
