# Simple test case to test a trivial ``divided`` function.
import unittest


def divided(dividend, divisor):
    return dividend / divisor
    # To break a test case, change / to //.


class DivideTest(unittest.TestCase):
    def test_can_divide_positive_numbers(self):
        self.assertEqual(3, divided(15, 5))
        self.assertAlmostEqual(2.5, divided(5, 2))

    def test_can_divide_negative_numbers(self):
        self.assertEqual(-3, divided(15, -5))

    def test_can_divide_zero(self):
        self.assertEqual(0, divided(0, 1))
        self.assertEqual(0, divided(0, -1))
        self.assertEqual(0, divided(0, 123.45))

    def test_fails_on_zero_division(self):
        self.assertRaises(ZeroDivisionError, divided, 1, 0)


if __name__ == '__main__':
    unittest.main()
