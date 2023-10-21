import unittest
from Unit_tests.NumberCheck import number_in_interval


class TestNumberInterval(unittest.TestCase):

    def setUp(self) -> None:
        """
        Создаем интервал в который должно попадать число.
        Функция range включает первое число и не включает второе, поэтому первым задаем 26. Шаг по умолчанию - 1.
        """
        self.container = range(26, 100)

    def test_falls_into_interval(self):
        """
        Попадает ли переданное число в интервал (25;100)
        """
        self.assertIn(26, self.container)
        self.assertTrue(number_in_interval(26))

    def test_falls_into_interval_lower_bound(self):
        """
        Попадает ли переданное число в интервал (25;100)
        """
        self.assertNotIn(25, self.container)
        self.assertFalse(number_in_interval(25))

    def test_falls_into_interval_upper_bound(self):
        """
        Попадает ли переданное число в интервал (25;100)
        """
        self.assertNotIn(100, self.container)
        self.assertFalse(number_in_interval(100))

    def test_falls_into_interval_beyond_borders(self):
        """
        Попадает ли переданное число в интервал (25;100)
        """
        self.assertNotIn(150, self.container)
        self.assertFalse(number_in_interval(150))

    def test_falls_into_negative_interval(self):
        """
        Попадает ли переданное число в интервал (25;100)
        """
        self.assertNotIn(-26, self.container)
        self.assertFalse(number_in_interval(-26))
