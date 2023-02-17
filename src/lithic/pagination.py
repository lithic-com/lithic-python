# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, runtime_checkable

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPage", "AsyncPage", "SyncCursorPage", "AsyncCursorPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


@runtime_checkable
class CursorPageItem(Protocol):
    token: str


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_entries: int
    total_pages: int

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if not current_page < self.total_pages:
            return None
        return PageInfo(params={"page": current_page + 1})


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_entries: int
    total_pages: int

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if not current_page < self.total_pages:
            return None
        return PageInfo(params={"page": current_page + 1})


class SyncCursorPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    has_more: bool

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        if len(self.data) > 0:
            return None

        if is_forwards:
            item = cast(Any, self.data[-1])
            if not isinstance(item, CursorPageItem):
                # TODO emit warning log
                return None
            return PageInfo(params={"staring_after": item.token})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem):
                # TODO emit warning log
                return None
            return PageInfo(params={"ending_before": item.token})


class AsyncCursorPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    has_more: bool

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        if len(self.data) > 0:
            return None

        if is_forwards:
            item = cast(Any, self.data[-1])
            if not isinstance(item, CursorPageItem):
                # TODO emit warning log
                return None
            return PageInfo(params={"staring_after": item.token})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem):
                # TODO emit warning log
                return None
            return PageInfo(params={"ending_before": item.token})
