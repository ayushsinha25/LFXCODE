import unittest
from main import process_list 

class TestProcessList(unittest.TestCase):

    def test_length_not_multiple_of_10(self):
        result = process_list([1,2,3,4,5])
        self.assertEqual(result, "Error: The length of the list must be a multiple of 10.")

    def test_valid_input(self):
        expected_result = [1, 5, 7]
        result = process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(result, expected_result)

    def test_no_integer_input(self):
        result = process_list([])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()