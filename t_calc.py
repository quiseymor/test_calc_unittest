import unittest
from calc import add, minus, multiply, divide, percent, step, logarithm, factorial


class TestCalculator(unittest.TestCase):

    # Сложение
    def test_add(self):
        # Позитив
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

        # Негатив
        self.assertNotEqual(add(1, 1), 3)

    # Вычитание
    def test_minus(self):
        # Позитив
        self.assertEqual(minus(10, 5), 5)
        self.assertEqual(minus(5, 10), -5)

        # Негатив
        self.assertNotEqual(minus(5, 3), 1)

    # Умножение
    def test_multiply(self):
        # Позитив
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 1), -1)

        # Негатив
        self.assertNotEqual(multiply(0, 5), 5)

    # Деление
    def test_divide(self):
        # Позитив
        self.assertEqual(divide(10, 5), 2)

        # Негатив
        self.assertEqual(divide(5, 0), "Ошибка: деление на нуль!")
        self.assertNotEqual(divide(10, 5), 3)

    # Проценты
    def test_percent(self):
        # Позитив
        self.assertEqual(percent(100, 20), 20)

        # Негатив
        self.assertNotEqual(percent(50, 100), 200)

    # Возведение в степень
    def test_step(self):
        # Позитив
        self.assertEqual(step(2, 3), 8)
        self.assertEqual(step(2, 0), 1)

        # Негатив
        self.assertNotEqual(step(2, 3), 7)

    # Логарифм
    def test_logarithm(self):
        # Позитив
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(1, 10), 0)

        # Негатив
        self.assertEqual(logarithm(-1), "Ошибка: логарифм не определён для неположительных чисел!")

    # Факториал
    def test_factorial(self):
        # Позитив
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

        # Негатив
        self.assertEqual(factorial(-1), "Ошибка: факториал не определён для отрицательных чисел!")


if __name__ == '__main__':
    unittest.main()
