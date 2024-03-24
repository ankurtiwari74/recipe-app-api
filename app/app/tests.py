"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc function."""

    def test_add_numbers(self):
        """Test adding two numbers."""
        result = calc.add(5, 6)
        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        result = calc.subtract(10, 15)
        self.assertEqual(result, 5)
