from __future__ import annotations

from typing import TypeVar, Iterable

_T = TypeVar("_T")


def flatten(t: Iterable[Iterable[_T]]) -> list[_T]:
    return [item for sublist in t for item in sublist]
