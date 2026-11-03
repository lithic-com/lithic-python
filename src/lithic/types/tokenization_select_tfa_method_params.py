# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenizationSelectTfaMethodParams"]


class TokenizationSelectTfaMethodParams(TypedDict, total=False):
    method: Required[Literal["SMS", "EMAIL"]]
    """An available method from the tokenization's list of tfa_methods"""
