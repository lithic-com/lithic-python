# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncCursorPage", "AsyncCursorPage", "SyncSinglePage", "AsyncSinglePage"]

_T = TypeVar("_T")


@runtime_checkable
class CursorPageItem(Protocol):
    token: Optional[str]


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    has_more: bool

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        return has_more and super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        data = self.data
        if not data:
            return None

        if is_forwards:
            item = cast(Any, data[-1])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"starting_after": item.token})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"ending_before": item.token})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    has_more: bool

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        return has_more and super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        data = self.data
        if not data:
            return None

        if is_forwards:
            item = cast(Any, data[-1])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"starting_after": item.token})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"ending_before": item.token})


class SyncSinglePage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    has_more: bool

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        return has_more and super().has_next_page()

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class AsyncSinglePage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    has_more: bool

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        return has_more and super().has_next_page()

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None
