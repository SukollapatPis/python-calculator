import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # acual output, expected output
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)


    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(8, 3), 2)
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(8, 1), 8)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(8, 4), 0)
        self.assertEqual(self.calc.modulo(8, 3), 2)
        self.assertEqual(self.calc.modulo(8, 2), 0)
        self.assertEqual(self.calc.modulo(8, 1), 0)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()