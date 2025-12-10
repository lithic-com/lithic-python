# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .three_ds_authentication import ThreeDSAuthentication

__all__ = ["ThreeDSAuthenticationChallengeWebhookEvent", "Challenge"]


class Challenge(BaseModel):
    """Represents a challenge object for 3DS authentication"""

    challenge_method_type: Literal["OUT_OF_BAND"]
    """The type of challenge method issued to the cardholder"""

    expiry_time: datetime
    """ISO-8601 time at which the challenge expires"""

    start_time: datetime
    """ISO-8601 time at which the challenge has started"""

    app_requestor_url: Optional[str] = None
    """Fully qualified app URL of the merchant app.

    This should be used to redirect the cardholder back to the merchant app after
    completing an app-based challenge. This URL will only be populated if the 3DS
    Requestor App is provided to the 3DS SDK.
    """


class ThreeDSAuthenticationChallengeWebhookEvent(BaseModel):
    authentication_object: ThreeDSAuthentication
    """Represents a 3DS authentication"""

    challenge: Challenge
    """Represents a challenge object for 3DS authentication"""

    event_type: Literal["three_ds_authentication.challenge"]
