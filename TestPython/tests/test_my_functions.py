import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src import my_functions


class TestMyFunctions(unittest.TestCase):
    def test_add_ok(self):
        result = my_functions.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_err(self):
        result = my_functions.add(3, 3)
        self.assertNotEqual(result, 5)

    def test_divide(self):
        result = my_functions.divide(10, 2)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
