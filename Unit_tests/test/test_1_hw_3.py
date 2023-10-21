import unittest
from Unit_tests.NumberCheck import even_odd_number


class TestUserNumber(unittest.TestCase):

    def test_even_parity_number(self):
        """
        Проверка на четность положительного четного числа
        """
        self.assertTrue(even_odd_number(2))

    def test_even_odd_number(self):
        """
        Проверка на четность положительного нечетного числа
        """
        self.assertFalse(even_odd_number(3))

    def test_even_negative_parity_number(self):
        """
        Проверка на четность отрицательного четного числа
        """
        self.assertTrue(even_odd_number(-2))

    def test_even_negative_odd_number(self):
        """
        Проверка на четность отрицательного нечетного числа
        """
        self.assertFalse(even_odd_number(-3))

    def test_even_zero(self):
        """
        Проверка на четность ноля
        """
        self.assertTrue(even_odd_number(0))
        