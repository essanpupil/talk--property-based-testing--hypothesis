from hypothesis import given
from hypothesis.strategies import integers


def csum_to(n):
    if n == 0:
        return [n]
    elif n == 1:
        return [0, 1]
    else:
        return [0] * (n+1)


@given(integers(min_value=0))
def test_csum_prop(n):
    s_n = csum_to(n)
    assert len(s_n) == n+1
    assert s_n[0] == 0
    assert s_n[-1] == sum(range(n+1))
