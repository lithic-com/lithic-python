from typing import Any, Dict, List, Optional, cast

import pytest
from pydantic import Field

from lithic._models import BaseModel

# TODO: test mismatched input and  field types


class BasicModel(BaseModel):
    foo: str


def test_basic() -> None:
    m = BasicModel.construct(foo="hello")
    assert m.foo == "hello"


def test_directly_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: BasicModel

    m = NestedModel.construct(nested={"foo": "Foo!"})
    assert m.nested.foo == "Foo!"


def test_optional_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: Optional[BasicModel]

    m1 = NestedModel.construct(nested=None)
    assert m1.nested is None

    m2 = NestedModel.construct(nested={"foo": "bar"})
    assert m2.nested is not None
    assert m2.nested.foo == "bar"


def test_list_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: List[BasicModel]

    m = NestedModel.construct(nested=[{"foo": "bar"}, {"foo": "2"}])
    assert m.nested is not None
    assert isinstance(m.nested, list)
    assert len(m.nested) == 2
    assert m.nested[0].foo == "bar"
    assert m.nested[1].foo == "2"


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


def test_raw_dictionary() -> None:
    class NestedModel(BaseModel):
        nested: Dict[str, str]

    m = NestedModel.construct(nested={"hello": "world"})
    assert m.nested == {"hello": "world"}


@pytest.mark.skip(reason="We do not support nested dictionary models yet")
def test_nested_dictionary_model() -> None:
    class NestedModel(BaseModel):
        nested: Dict[str, BasicModel]

    m = NestedModel.construct(nested={"hello": {"foo": "bar"}})
    assert isinstance(m.nested, dict)
    assert m.nested["hello"].foo == "bar"


@pytest.mark.skip(reason="Unknown fields are not supported yet")
def test_unknown_fields() -> None:
    m = BasicModel.construct(foo="foo", unknown=1)
    assert m.foo == "foo"
    assert cast(Any, m).unknown == 1


def test_aliases() -> None:
    class Model(BaseModel):
        my_field: int = Field(alias="myField")

    m = Model.construct(myField=1)
    assert m.my_field == 1
