from mycalc import add, mul


def test_add():
    assert add(2, 3) == 5


def test_mul():
    assert mul(4, 6) == 24
