import unittest
from mathfunct import *


class TestMathFunct(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, add(1,2))
        self.assertNotEqual(3, add(2,2))

    def test_minus(self):
        self.assertEqual(3, minus(5,2))
        self.assertNotEqual(3, minus(6,2))
    
    def test_multi(self):
        self.assertEqual(10, multi(5,2))
        self.assertNotEqual(15, multi(6,2))

    def test_divide(self):
        self.assertEqual(5, divide(10,2))
        self.assertNotEqual(14, divide(6,2))
    
if __name__ == '__main__':
    unittest.main()