from hypothesis import given
from hypothesis.strategies import integers


def csum_to(n):
    return [sum(range(i)) for i in range(n+1)]


@given(integers(min_value=0, max_value=100))
def test_csum_prop(n):
    s_n = csum_to(n)
    assert len(s_n) == n+1
    assert s_n[0] == 0
    assert s_n[-1] == sum(range(n+1))
