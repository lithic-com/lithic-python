from typing import Any, Dict, List, Optional, cast

import pytest
from pydantic import Field

from lithic._models import BaseModel


class BasicModel(BaseModel):
    foo: str


@pytest.mark.parametrize("value", ["hello", 1], ids=["correct type", "mismatched"])
def test_basic(value: object) -> None:
    m = BasicModel.construct(foo=value)
    assert m.foo == value


def test_directly_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: BasicModel

    m = NestedModel.construct(nested={"foo": "Foo!"})
    assert m.nested.foo == "Foo!"

    # mismatched types
    m = NestedModel.construct(nested="hello!")
    assert m.nested == "hello!"


def test_optional_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: Optional[BasicModel]

    m1 = NestedModel.construct(nested=None)
    assert m1.nested is None

    m2 = NestedModel.construct(nested={"foo": "bar"})
    assert m2.nested is not None
    assert m2.nested.foo == "bar"

    # mismatched types
    m3 = NestedModel.construct(nested={"foo"})
    assert isinstance(cast(Any, m3.nested), set)
    assert m3.nested == {"foo"}


def test_list_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: List[BasicModel]

    m = NestedModel.construct(nested=[{"foo": "bar"}, {"foo": "2"}])
    assert m.nested is not None
    assert isinstance(m.nested, list)
    assert len(m.nested) == 2
    assert m.nested[0].foo == "bar"
    assert m.nested[1].foo == "2"

    # mismatched types
    m = NestedModel.construct(nested=True)
    assert cast(Any, m.nested) is True

    m = NestedModel.construct(nested=[False])
    assert cast(Any, m.nested) == [False]


def test_optional_list_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: Optional[List[BasicModel]]

    m1 = NestedModel.construct(nested=[{"foo": "bar"}, {"foo": "2"}])
    assert m1.nested is not None
    assert isinstance(m1.nested, list)
    assert len(m1.nested) == 2
    assert m1.nested[0].foo == "bar"
    assert m1.nested[1].foo == "2"

    m2 = NestedModel.construct(nested=None)
    assert m2.nested is None

    # mismatched types
    m3 = NestedModel.construct(nested={1})
    assert cast(Any, m3.nested) == {1}

    m4 = NestedModel.construct(nested=[False])
    assert cast(Any, m4.nested) == [False]


def test_list_optional_items_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: List[Optional[BasicModel]]

    m = NestedModel.construct(nested=[None, {"foo": "bar"}])
    assert m.nested is not None
    assert isinstance(m.nested, list)
    assert len(m.nested) == 2
    assert m.nested[0] is None
    assert m.nested[1] is not None
    assert m.nested[1].foo == "bar"

    # mismatched types
    m3 = NestedModel.construct(nested="foo")
    assert cast(Any, m3.nested) == "foo"

    m4 = NestedModel.construct(nested=[False])
    assert cast(Any, m4.nested) == [False]


def test_raw_dictionary() -> None:
    class NestedModel(BaseModel):
        nested: Dict[str, str]

    m = NestedModel.construct(nested={"hello": "world"})
    assert m.nested == {"hello": "world"}

    # mismatched types
    m = NestedModel.construct(nested=False)
    assert cast(Any, m.nested) is False


@pytest.mark.skip(reason="We do not support nested dictionary models yet")
def test_nested_dictionary_model() -> None:
    class NestedModel(BaseModel):
        nested: Dict[str, BasicModel]

    m = NestedModel.construct(nested={"hello": {"foo": "bar"}})
    assert isinstance(m.nested, dict)
    assert m.nested["hello"].foo == "bar"

    # mismatched types
    m = NestedModel.construct(nested={"hello": False})
    assert cast(Any, m.nested["hello"]) is False


def test_unknown_fields() -> None:
    m1 = BasicModel.construct(foo="foo", unknown=1)
    assert m1.foo == "foo"
    assert cast(Any, m1).unknown == 1

    m2 = BasicModel.construct(foo="foo", unknown={"foo_bar": True})
    assert m2.foo == "foo"
    assert cast(Any, m2).unknown == {"foo_bar": True}


def test_aliases() -> None:
    class Model(BaseModel):
        my_field: int = Field(alias="myField")

    m = Model.construct(myField=1)
    assert m.my_field == 1

    # mismatched types
    m = Model.construct(myField={"hello": False})
    assert cast(Any, m.my_field) == {"hello": False}


def test_repr() -> None:
    model = BasicModel(foo="bar")
    assert str(model) == "BasicModel(foo='bar')"
    assert repr(model) == "BasicModel(foo='bar')"


def test_repr_nested_model() -> None:
    class Child(BaseModel):
        name: str
        age: int

    class Parent(BaseModel):
        name: str
        child: Child

    model = Parent(name="Robert", child=Child(name="Foo", age=5))
    assert str(model) == "Parent(name='Robert', child=Child(name='Foo', age=5))"
    assert repr(model) == "Parent(name='Robert', child=Child(name='Foo', age=5))"
