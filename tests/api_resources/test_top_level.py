# File generated from our OpenAPI spec by Stainless.
import os
import pytest
from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage

from lithic.types.shipping_address import *


base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTopLevel:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)


class TestAsyncTopLevel:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
