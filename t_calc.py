import unittest
from calc import add, minus, multiply, divide, percent, step, logarithm, factorial

class TestCalculator(unittest.TestCase):

    def test_add(self):
        print("Верный тест: ")
        print("Тест сложения: 10 + 5 = 15")
        self.assertEqual(add(10, 5), 15)
        print("Тест сложения: -1 + 1 = 0")
        self.assertEqual(add(-1, 1), 0)
        print("Неверный тест: ")
        print("Тест сложения: 1 + 1 = 3")
        self.assertNotEqual(add(1, 1), 3)

    def test_minus(self):
        print("Верный тест: ")
        print("Тест вычитания: 10 - 5 = 5")
        self.assertEqual(minus(10, 5), 5)
        print("Тест вычитания: 5 - 10 = -5")
        self.assertEqual(minus(5, 10), -5)
        print("Неверный тест: ")
        print("Тест вычитания: 5 - 3 = 1")
        self.assertNotEqual(minus(5, 3), 1)

    def test_multiply(self):
        print("Верный тест: ")
        print("Тест умножения: 3 * 5 = 15")
        self.assertEqual(multiply(3, 5), 15)
        print("Тест умножения: -1 * 1 = -1")
        self.assertEqual(multiply(-1, 1), -1)
        print("Неверный тест: ")
        print("Тест умножения: 0 * 5 = 5")
        self.assertNotEqual(multiply(0, 5), 5)

    def test_divide(self):
        print("Верный тест: ")
        print("Тест деления: 10 / 5 = 2")
        self.assertEqual(divide(10, 5), 2)
        print("Тест деления: 5 / 0 = Ошибка: деление на нуль!")
        self.assertEqual(divide(5, 0), "Ошибка: деление на нуль!")
        print("Неверный тест: ")
        print("Тест деления: 10 / 5 = 3")
        self.assertNotEqual(divide(10, 5), 3)

    def test_percent(self):
        print("Верный тест: ")
        print("Тест процента: 20% от 100 = 20")
        self.assertEqual(percent(100, 20), 20)
        print("Неверный тест: ")
        print("Тест процента: 100% от 50 = 200")
        self.assertNotEqual(percent(50, 100), 200)

    def test_step(self):
        print("Верный тест: ")
        print("Тест возведения в степень: 2^3 = 8")
        self.assertEqual(step(2, 3), 8)
        print("Тест возведения в степень: 2^0 = 1")
        self.assertEqual(step(2, 0), 1)
        print("Неверный тест: ")
        print("Тест возведения в степень: 2^3 = 7")
        self.assertNotEqual(step(2, 3), 7)

    def test_logarithm(self):
        print("Верный тест: ")
        print("Тест логарифма: log10(100) = 2")
        self.assertAlmostEqual(logarithm(100, 10), 2)
        print("Тест логарифма: log10(1) = 0")
        self.assertAlmostEqual(logarithm(1, 10), 0)
        print("Неверный тест: ")
        print("Тест логарифма: log(-1) = Ошибка: логарифм не определён для неположительных чисел!")
        self.assertEqual(logarithm(-1), "Ошибка: логарифм не определён для неположительных чисел!")

    def test_factorial(self):
        print("Верный тест: ")
        print("Тест факториала: 5! = 120")
        self.assertEqual(factorial(5), 120)
        print("Тест факториала: 0! = 1")
        self.assertEqual(factorial(0), 1)
        print("Неверный тест: ")
        print("Тест факториала: (-1)! = Ошибка: факториал не определён для отрицательных чисел!")
        self.assertEqual(factorial(-1), "Ошибка: факториал не определён для отрицательных чисел!")

if __name__ == '__main__':
    unittest.main()
