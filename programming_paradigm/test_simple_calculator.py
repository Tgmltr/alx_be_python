import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertNotEqual(self.calc.add(-1, 1), 1)
    def test_substraction(self):
        self.assertEqual(self.calc.subtract(4,2),2)
        self.assertEqual(self.calc.subtract(0,0),0)
        self.assertEqual(self.calc.subtract(-2,4),-6)
        self.assertNotEqual(self.calc.subtract(-2,4),0)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4,2),8)
        self.assertEqual(self.calc.multiply(0,1),0)
        self.assertEqual(self.calc.multiply(-2,4),-8)
        self.assertNotEqual(self.calc.multiply(-2,4),0)
    def test_division(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(-2,4),-0.5)
        self.assertNotEqual(self.calc.divide(-2,4),0)
    def test_div_by_zero(self):
        try:
            self.calc.divide(-2,0)
        except Exception:
            print(f"division by zero impossible")
        else:
            self.assertEqual(self.calc.divide(-2,1), -2)
