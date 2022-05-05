# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict
from .._core import Timeout, make_request_options
from .._resource import SyncAPIResource, AsyncAPIResource
from .._models import StringModel, NoneModel
from ..pagination import SyncPage, AsyncPage
from ..types.funding_source import *
from ..types.funding_source_create_params import *
from ..types.funding_source_update_params import *
from ..types.funding_source_list_params import *
from ..types.funding_source_verify_params import *

__all__ = ["FundingSources", "AsyncFundingSources"]


class FundingSources(SyncAPIResource):
    def create(
        self,
        body: FundingSourceCreateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> FundingSource:
        """Add a funding source using bank routing and account numbers or via
        Plaid.

        In the production environment, funding accounts will be set to
        `PENDING` state until micro-deposit validation completes while
        funding accounts in sandbox will be set to `ENABLED` state
        automatically.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post("/funding_sources", model=FundingSource, body=body, options=options)

    def update(
        self,
        id: str,
        body: FundingSourceUpdateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> FundingSource:
        """Update a funding source."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.patch(f"/funding_sources/{id}", model=FundingSource, body=body, options=options)

    def list(
        self,
        query: Optional[FundingSourceListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> SyncPage[FundingSource]:
        """List all the funding sources associated with the Lithic account."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get_api_list(
            "/funding_sources", model=FundingSource, page=SyncPage[FundingSource], query=query, options=options
        )

    def verify(
        self,
        id: str,
        body: FundingSourceVerifyParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> FundingSource:
        """Verify a bank account as a funding source by providing received
        micro-deposit amounts."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post(f"/funding_sources/{id}/verify", model=FundingSource, body=body, options=options)


class AsyncFundingSources(AsyncAPIResource):
    async def create(
        self,
        body: FundingSourceCreateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> FundingSource:
        """Add a funding source using bank routing and account numbers or via
        Plaid.

        In the production environment, funding accounts will be set to
        `PENDING` state until micro-deposit validation completes while
        funding accounts in sandbox will be set to `ENABLED` state
        automatically.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post("/funding_sources", model=FundingSource, body=body, options=options)

    async def update(
        self,
        id: str,
        body: FundingSourceUpdateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> FundingSource:
        """Update a funding source."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.patch(f"/funding_sources/{id}", model=FundingSource, body=body, options=options)

    def list(
        self,
        query: Optional[FundingSourceListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AsyncPage[FundingSource]:
        """List all the funding sources associated with the Lithic account."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get_api_list(
            "/funding_sources", model=FundingSource, page=AsyncPage[FundingSource], query=query, options=options
        )

    async def verify(
        self,
        id: str,
        body: FundingSourceVerifyParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> FundingSource:
        """Verify a bank account as a funding source by providing received
        micro-deposit amounts."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post(f"/funding_sources/{id}/verify", model=FundingSource, body=body, options=options)
