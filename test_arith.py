from hypothesis import given
from hypothesis.strategies import (
    integers,
    floats
)
from pytest import raises


@given(x=integers())
def test_div_by_zero(x):
    with raises(ZeroDivisionError):
        x / 0


@given(integers())
def test_negation_is_self_inverse_int(x):
    assert x == -(-x)


@given(floats())
def test_negation_is_self_inverse_float(x):
    assert x == -(-x)
