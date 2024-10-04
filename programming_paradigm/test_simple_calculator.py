import unittest
from simple_calculator import SimpleCalculator 


class testcalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self)(self):
        self.assertEqual(self.calc.add(2,3),5)

    def test_subtraction(self)(self):
        self.assertEqual(self.calc.subtract(5,3),2)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,4),20)

    def test_division(self):
        self.assertEqual(self.calc.divide(30,5),6)
        self.assertEqual(self.calc.divide(30,0),'Error: Cannot divide by zero.')


if __name__ == '__main__':
    unittest.main()  # Run the tests
    
    