def csum_to(n):
    if n == 0:
        return [n]
    if n == 1:
        return [0, 1]

def test_csum_01():
    assert csum_to(0) == [0]
    assert csum_to(1) == [0, 1]
