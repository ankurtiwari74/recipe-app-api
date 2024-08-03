"""
Sample tests
"""
from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Tests for `calc` module."""

    def test_add_numbers(self):
        """Test the addition of two numbers."""
        res = calc.add(1, 2)
        self.assertEqual(res, 3)

    def test_subtract_numbers(self):
        """Test the subtraction of two numbers."""
        res = calc.subtract(1, 2)
        self.assertEqual(res, -1)
