import unittest
import pythonTest

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = pythonTest.calculate("1 1 +")
        self.assertEqual(2, result)
