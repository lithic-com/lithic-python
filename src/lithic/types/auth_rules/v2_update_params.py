# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V2UpdateParams"]


class V2UpdateParams(TypedDict, total=False):
    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """
