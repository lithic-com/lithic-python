from __future__ import annotations

from typing import Any, Mapping, TypeVar
from typing_extensions import get_args, get_type_hints

from pydantic.typing import is_typeddict

from ._utils import (
    is_list,
    is_mapping,
    is_list_type,
    is_union_type,
    extract_type_arg,
    is_required_type,
    is_annotated_type,
    strip_annotated_type,
)

_T = TypeVar("_T")


# TODO: support for drilling globals() and locals()
# TODO: ensure works correctly with forward references in all cases


class PropertyInfo:
    """Metadata class to be used in Annotated types to provide information about a given type.

    For example:

    class MyParams(TypedDict):
        account_holder_name: Annotated[str, PropertyInfo(alias='accountHolderName')]

    This means that {'account_holder_name': 'Robert'} will be transformed to {'accountHolderName': 'Robert'} before being sent to the API.
    """

    alias: str

    def __init__(self, *, alias: str) -> None:
        self.alias = alias

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(alias='{self.alias}')"


def maybe_transform(
    data: Mapping[str, object] | None,
    expected_type: object,
) -> Any | None:
    """Wrapper over `transform()` that allows `None` to be passed.

    See `transform()` for more details.
    """
    if data is None:
        return None
    return transform(data, expected_type)


# Wrapper over _transform_recursive providing fake types
def transform(
    data: _T,
    expected_type: object,
) -> _T:
    """Transform dictionary keys based off of type information from the given type, for example:

    ```py
    class Params(TypedDict, total=False):
        card_id: Required[Annotated[str, PropertyInfo(alias='cardID')]]

    transformed = transform({'card_id': '<my card ID>'}, Params)
    # {'cardID': '<my card ID>'}
    ```

    Any keys / data that does not have type information given will be included as is.
    """
    return _transform_recursive(data, expected_type)  # type: ignore


def _maybe_transform_key(key: str, annotation: type) -> str:
    if is_required_type(annotation):
        annotation = get_args(annotation)[0]

    if not is_annotated_type(annotation):
        return key

    # ignore the first argument as it is the actual type
    args = get_args(annotation)[1:]
    for arg in args:
        if isinstance(arg, PropertyInfo):
            return arg.alias
    return key


def _transform_recursive(data: object, typ: type) -> object:
    stripped_type = strip_annotated_type(typ)
    if is_typeddict(stripped_type) and is_mapping(data):
        return _transform_typeddict(data, stripped_type)

    if is_list_type(stripped_type) and is_list(data):
        inner_type = extract_type_arg(stripped_type, 0)
        return [_transform_recursive(d, inner_type) for d in data]

    if is_union_type(stripped_type):
        # For union types we run the transformation against all subtypes to ensure that everything is transformed.
        #
        # TODO: there may be edge cases where the same normalized field name will transform to two different names
        # in different subtypes.
        for subtype in get_args(stripped_type):
            data = _transform_recursive(data, subtype)
        return data

    return data


def _transform_typeddict(
    data: Mapping[str, object],
    expected_type: type,
) -> Mapping[str, object]:
    result: dict[str, object] = {}
    annotations = get_type_hints(expected_type, include_extras=True)
    for key, value in data.items():
        typ = annotations.get(key)
        if typ is None:
            # we do not have a type annotation for this field, leave it as is
            result[key] = value
        else:
            result[_maybe_transform_key(key, typ)] = _transform_recursive(value, typ)
    return result
