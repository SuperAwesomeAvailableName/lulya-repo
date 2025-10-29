import unittest
from calculate_average import calculate_average


class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_normal_case(self):
        """Test the calculate_average function with normal input."""
        numbers = [1.5, 2.5, 3.5, 4.5]
        result = calculate_average(numbers)
        self.assertEqual(result, 3.0)

    def test_calculate_average_single_value(self):
        """Test the calculate_average function with a single value."""
        numbers = [42.0]
        result = calculate_average(numbers)
        self.assertEqual(result, 42.0)

    def test_calculate_average_empty_list(self):
        """Test that calculate_average raises ValueError for empty list."""
        with self.assertRaises(ValueError):
            calculate_average([])


if __name__ == '__main__':
    unittest.main()

# Hi this indicates custom guidelines working
