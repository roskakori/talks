# Test a division function using pytest.
def divided(dividend, divisor):
    return dividend / divisor


def assert_almost_equal(a, b, places=7):
    assert round(abs(a - b), places) == 0


def test_can_divide_positive_numbers():
    assert 3 == divided(15, 5)
    assert_almost_equal(2.5, divided(5, 2))


def test_can_divide_negative_numbers():
    assert -3 == divided(15, -5)


def test_can_divide_zero():
    assert 0 == divided(0, 1)
    assert 0 == divided(0, -1)
    assert 0 == divided(0, 123.45)