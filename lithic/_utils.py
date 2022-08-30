from __future__ import annotations

from typing import Mapping, TypeVar, Iterable, Sequence, cast
from typing_extensions import TypeGuard

from ._types import FileTypes

_T = TypeVar("_T")


def flatten(t: Iterable[Iterable[_T]]) -> list[_T]:
    return [item for sublist in t for item in sublist]


def extract_files(
    # TODO: this needs to take Dict but variance issues.....
    # create protocol type ?
    query: Mapping[str, object],
    *,
    paths: Sequence[Sequence[str]],
) -> list[tuple[str, FileTypes]]:
    files: list[tuple[str, FileTypes]] = []
    for path in paths:
        files.extend(_extract_items(query, path, index=0, flattened_key=None))
    return files


def _extract_items(
    obj: object,
    path: Sequence[str],
    *,
    index: int,
    # TODO: rename
    flattened_key: str | None,
) -> list[tuple[str, FileTypes]]:
    try:
        key = path[index]
    except IndexError:
        # We have exhausted the path, return the entry we found.
        if not isinstance(obj, bytes) and not isinstance(obj, tuple):
            raise RuntimeError(
                f"Expected entry at {flattened_key} to be bytes or a tuple but received {type(obj)} instead."
            )

        # TODO: validate obj more?
        assert flattened_key is not None
        return [(flattened_key, cast(FileTypes, obj))]

    index += 1
    if is_dict(obj):
        try:
            # We are at the last entry in the path so we must remove the field
            if (len(path)) == index:
                item = obj.pop(key)
            else:
                item = obj[key]
        except KeyError:
            # Key was not present in the dictionary, this is not indicative of an error
            # as the given path may not point to a required field. We also do not want
            # to enforce required fields as the API may differ from the spec in some cases.
            return []
        if flattened_key is None:
            flattened_key = key
        else:
            flattened_key += f"[{key}]"
        return _extract_items(
            item,
            path,
            index=index,
            flattened_key=flattened_key,
        )
    elif is_list(obj):
        if key != "<array>":
            return []

        return flatten(
            [
                _extract_items(
                    item,
                    path,
                    index=index,
                    flattened_key=flattened_key + "[]" if flattened_key is not None else "[]",
                )
                for item in obj
            ]
        )

    # Something unexpected was passed, just ignore it.
    return []


# Type safe methods for narrowing types with TypeVars.
# The default narrowing for isinstance(obj, dict) is dict[unknown, unknown],
# however this cause Pyright to rightfully report errors. As we know we don't
# care about the contained types we can safely use `object` in it's place.


def is_dict(obj: object) -> TypeGuard[dict[object, object]]:
    return isinstance(obj, dict)


def is_list(obj: object) -> TypeGuard[list[object]]:
    return isinstance(obj, list)
