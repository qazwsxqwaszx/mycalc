from mycalc import add, mul, sub, div


def test_add():
    assert add(2, 3) == 5


def test_mul():
    assert mul(4, 6) == 24


def test_sub():
    assert sub(10, 4) == 6


def test_div():
    assert div(12, 3) == 4
