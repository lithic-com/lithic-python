# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CardWebProvisionResponse", "Jws", "JwsHeader"]


class JwsHeader(BaseModel):
    kid: Optional[str] = None
    """The ID for the JWS Public Key of the key pair used to generate the signature."""


class Jws(BaseModel):
    header: Optional[JwsHeader] = None
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


class CardWebProvisionResponse(BaseModel):
    jws: Optional[Jws] = None
    """JWS object required for handoff to Apple's script."""

    state: Optional[str] = None
    """A unique identifier for the JWS object."""
