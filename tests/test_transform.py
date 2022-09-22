from __future__ import annotations

from typing import List, Union
from typing_extensions import Annotated, TypedDict

from lithic._utils import PropertyInfo, transform


class Foo1(TypedDict):
    foo_bar: Annotated[str, PropertyInfo(alias="fooBar")]


def test_top_level_alias() -> None:
    assert transform({"foo_bar": "hello"}, expected_type=Foo1) == {"fooBar": "hello"}


class Foo2(TypedDict):
    bar: Bar2


class Bar2(TypedDict):
    this_thing: Annotated[int, PropertyInfo(alias="this__thing")]
    baz: Annotated[Baz2, PropertyInfo(alias="Baz")]


class Baz2(TypedDict):
    my_baz: Annotated[str, PropertyInfo(alias="myBaz")]


def test_recursive_typeddict() -> None:
    assert transform({"bar": {"this_thing": 1}}, Foo2) == {"bar": {"this__thing": 1}}
    assert transform({"bar": {"baz": {"my_baz": "foo"}}}, Foo2) == {"bar": {"Baz": {"myBaz": "foo"}}}


class Foo3(TypedDict):
    things: List[Bar3]


class Bar3(TypedDict):
    my_field: Annotated[str, PropertyInfo(alias="myField")]


def test_list_of_typeddict() -> None:
    result = transform({"things": [{"my_field": "foo"}, {"my_field": "foo2"}]}, expected_type=Foo3)
    assert result == {"things": [{"myField": "foo"}, {"myField": "foo2"}]}


class Foo4(TypedDict):
    foo: Union[Bar4, Baz4]


class Bar4(TypedDict):
    foo_bar: Annotated[str, PropertyInfo(alias="fooBar")]


class Baz4(TypedDict):
    foo_baz: Annotated[str, PropertyInfo(alias="fooBaz")]


def test_union_of_typeddict() -> None:
    assert transform({"foo": {"foo_bar": "bar"}}, Foo4) == {"foo": {"fooBar": "bar"}}
    assert transform({"foo": {"foo_baz": "baz"}}, Foo4) == {"foo": {"fooBaz": "baz"}}
    assert transform({"foo": {"foo_baz": "baz", "foo_bar": "bar"}}, Foo4) == {"foo": {"fooBaz": "baz", "fooBar": "bar"}}


class Foo5(TypedDict):
    foo: Annotated[Union[Bar4, List[Baz4]], PropertyInfo(alias="FOO")]


class Bar5(TypedDict):
    foo_bar: Annotated[str, PropertyInfo(alias="fooBar")]


class Baz5(TypedDict):
    foo_baz: Annotated[str, PropertyInfo(alias="fooBaz")]


def test_union_of_list() -> None:
    assert transform({"foo": {"foo_bar": "bar"}}, Foo5) == {"FOO": {"fooBar": "bar"}}
    assert transform(
        {
            "foo": [
                {"foo_baz": "baz"},
                {"foo_baz": "baz"},
            ]
        },
        Foo5,
    ) == {"FOO": [{"fooBaz": "baz"}, {"fooBaz": "baz"}]}


class Foo6(TypedDict):
    bar: Annotated[str, PropertyInfo(alias="Bar")]


def test_includes_unknown_keys() -> None:
    assert transform({"bar": "bar", "baz_": {"FOO": 1}}, Foo6) == {"Bar": "bar", "baz_": {"FOO": 1}}


class Foo7(TypedDict):
    bar: Annotated[List[Bar7], PropertyInfo(alias="bAr")]
    foo: Bar7


class Bar7(TypedDict):
    foo: str


def test_ignores_invalid_input() -> None:
    assert transform({"bar": "<foo>"}, Foo7) == {"bAr": "<foo>"}
    assert transform({"foo": "<foo>"}, Foo7) == {"foo": "<foo>"}
