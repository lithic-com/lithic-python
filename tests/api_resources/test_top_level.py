# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from lithic import Lithic, AsyncLithic

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTopLevel:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)


class TestAsyncTopLevel:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
