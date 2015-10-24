def csum_to(n):
    if n == 0:
        return [n]


def test_csum_01():
    assert csum_to(0) == [0]
    assert csum_to(1) == [0, 1]
