# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .card_authorization import CardAuthorization

__all__ = ["CardAuthorizationApprovalRequestWebhookEvent"]


class CardAuthorizationApprovalRequestWebhookEvent(CardAuthorization):
    """The Auth Stream Access request payload that was sent to the ASA responder."""

    event_type: Literal["card_authorization.approval_request"]
