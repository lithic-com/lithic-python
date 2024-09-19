# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RequiredDocument"]


class RequiredDocument(BaseModel):
    entity_token: str
    """Globally unique identifier for an entity."""

    status_reasons: List[str]
    """
    rovides the status reasons that will be satisfied by providing one of the valid
    documents.
    """

    valid_documents: List[str]
    """
    A list of valid documents that will satisfy the KYC requirements for the
    specified entity.
    """
