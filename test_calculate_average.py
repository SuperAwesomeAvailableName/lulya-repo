import unittest
from calculate_average import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_normal_case(self):
        numbers = [1.5, 2.5, 3.5, 4.5]
        expected_result = 3.0
        self.assertEqual(calculate_average(numbers), expected_result)

    def test_calculate_average_single_number(self):
        numbers = [42.0]
        expected_result = 42.0
        self.assertEqual(calculate_average(numbers), expected_result)

    def test_calculate_average_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            calculate_average(numbers)

if __name__ == '__main__':
    unittest.main()

# Hi this indicates custom guidelines working
