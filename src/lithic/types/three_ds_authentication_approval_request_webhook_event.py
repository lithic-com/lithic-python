# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .three_ds_authentication import ThreeDSAuthentication

__all__ = ["ThreeDSAuthenticationApprovalRequestWebhookEvent"]


class ThreeDSAuthenticationApprovalRequestWebhookEvent(ThreeDSAuthentication):
    """Represents a 3DS authentication"""

    event_type: Literal["three_ds_authentication.approval_request"]
