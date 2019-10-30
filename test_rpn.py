import unittest
import pythonTest

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = pythonTest.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_sub(self):
        result = pythonTest.calculate("2 1 -")
        self.assertEqual(1, result)
    def test_mul(self):
        result = pythonTest.calculate("4 8 *")
        self.assertEqual(32, result)
    def test_badinput(self):
        with self.assertRaises(TypeError):
            pythonTest.calculate('1 2 3 +')
