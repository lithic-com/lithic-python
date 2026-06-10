# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentUpdateParams"]


class CommentUpdateParams(TypedDict, total=False):
    case_token: Required[str]

    comment: Required[str]
    """New text of the comment"""

    actor_token: str
    """
    Optional client-provided identifier for the actor performing this action,
    recorded on the resulting activity entry. This value is supplied by the client
    (for example, your own internal user ID) and is not authenticated by Lithic
    """
