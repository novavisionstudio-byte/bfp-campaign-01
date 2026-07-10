from app.gen_15 import value_15


def test_value_15():
    assert value_15(2) == 2 * 6 + 9
    assert value_15(0) == 9
