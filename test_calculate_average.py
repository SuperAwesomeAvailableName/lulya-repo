import unittest
from calculate_average import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average_normal(self):
        numbers = [1.5, 2.5, 3.5, 4.5]
        expected_result = 3.0
        self.assertEqual(calculate_average(numbers), expected_result)

    def test_calculate_average_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_calculate_average_single_element(self):
        numbers = [42.0]
        expected_result = 42.0
        self.assertEqual(calculate_average(numbers), expected_result)

if __name__ == '__main__':
    unittest.main()

# Hi this indicates custom guidelines working
