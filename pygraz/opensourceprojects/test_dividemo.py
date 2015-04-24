"""
Tests for dividemo.
"""
import unittest

from dividemo import dividemo

class DividemoTest(unittest.TestCase):
    def test_can_divide(self):
        self.assertEqual(2, dividemo.divided(10, 5))

    def test_can_print_divided(self):
        dividemo.main(['10', '5'])

    def test_fails_on_non_integer_divisor(self):
        self.assertRaises(SystemExit, dividemo.main, ['10', 'hello'])
