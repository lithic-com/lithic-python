# File generated from our OpenAPI spec by Stainless.

from typing import Optional, TypeVar, List, Generic, Dict, Any
from typing_extensions import TypedDict
from ._models import GenericModel
from ._core import FinalRequestOptions, BasePage
from ._client import SyncPage as BaseSyncPage, AsyncPage as BaseAsyncPage, Item

__all__ = ["PaginationParams", "SyncPage", "AsyncPage"]


class PaginationParams(TypedDict, total=False):
    page: int
    page_size: int


class Page(BasePage[Item, PaginationParams], Generic[Item]):
    data: List[Item]
    page: int
    total_pages: int
    total_entries: int

    def has_next_page(self) -> bool:
        return self.page < self.total_pages

    def _next_page_params(self):
        return {"page": self.page + 1}

    def _get_page_items(self):
        return self.data


class SyncPage(Page[Item], BaseSyncPage[Item, "SyncPage[Item]", PaginationParams], Generic[Item]):
    pass


class AsyncPage(Page[Item], BaseAsyncPage[Item, "AsyncPage[Item]", PaginationParams], Generic[Item]):
    pass
