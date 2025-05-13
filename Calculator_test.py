import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Инициализирует калькулятор для каждого теста."""
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 2), 1)
        self.assertEqual(self.calculator.add(2.5, 3.5), 6.0)


    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(2, 5), -3)
        self.assertEqual(self.calculator.subtract(2.5, 1.5), 1.0)
    

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(2.5, 2), 5.0)


    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5.0)
        self.assertEqual(self.calculator.divide(5, 1), 5.0)
        self.assertEqual(self.calculator.divide(4.0, 2.0), 2.0)


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)


    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calculator.add("a", 2)
        with self.assertRaises(TypeError):
            self.calculator.subtract(2, "b")
        with self.assertRaises(TypeError):
           self.calculator.multiply(2, "a")
        with self.assertRaises(TypeError):
          self.calculator.divide(2, "a")




if __name__ == '__main__':
    unittest.main()