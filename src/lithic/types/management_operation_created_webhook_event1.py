# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .management_operation_transaction import ManagementOperationTransaction

__all__ = ["ManagementOperationCreatedWebhookEvent"]


class ManagementOperationCreatedWebhookEvent(ManagementOperationTransaction):
    event_type: Literal["management_operation.created"]
    """The type of event that occurred."""
