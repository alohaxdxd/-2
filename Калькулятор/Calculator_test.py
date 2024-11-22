import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    Тестовый класс для проверки функциональности класса Calculator.
    """

    def setUp(self):
        """
        Инициализация тестового экземпляра класса Calculator перед каждым тестом.
        """
        self.calculator = Calculator()

    def test_add(self):
        """Тесты для метода add."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-2, 3), 1)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(-5, -5), -10)
        self.assertEqual(self.calculator.add(100, 200), 300)

    def test_subtract(self):
        """Тесты для метода subtract."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(3, 5), -2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(-5, -3), -2)
        self.assertEqual(self.calculator.subtract(100, 50), 50)

    def test_multiply(self):
        """Тесты для метода multiply."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(-5, -3), 15)
        self.assertEqual(self.calculator.multiply(10, 10), 100)

    def test_divide(self):
        """Тесты для метода divide."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-10, 2), -5)
        self.assertEqual(self.calculator.divide(10, -2), -5)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(0, 0)


if __name__ == '__main__':
    unittest.main()