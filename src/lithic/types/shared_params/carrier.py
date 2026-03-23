# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Carrier"]


class Carrier(TypedDict, total=False):
    qr_code_url: str
    """QR code URL to display on the card carrier.

    The `qr_code_url` field requires your domain to be allowlisted by Lithic before
    use. Contact Support to configure your QR code domain
    """
