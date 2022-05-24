# File generated from our OpenAPI spec by Stainless.

from typing import Any, Dict, List, Generic, TypeVar, Optional

from typing_extensions import TypedDict

from ._types import ModelT, FinalRequestOptions
from ._models import GenericModel
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage

__all__ = ["PaginationParams", "SyncPage", "AsyncPage"]


class PaginationParams(TypedDict, total=False):
    page: int
    page_size: int


class Page(BasePage[ModelT, PaginationParams], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_pages: int
    total_entries: int

    def has_next_page(self) -> bool:
        return self.page < self.total_pages

    def _next_page_params(self) -> PaginationParams:
        return {"page": self.page + 1}

    def _get_page_items(self) -> List[ModelT]:
        return self.data


class SyncPage(Page[ModelT], BaseSyncPage[ModelT], Generic[ModelT]):
    pass


class AsyncPage(Page[ModelT], BaseAsyncPage[ModelT], Generic[ModelT]):
    pass
