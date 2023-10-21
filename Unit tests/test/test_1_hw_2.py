import unittest

from Vehicle import Car, Motorcycle, Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        """
        Вызов метода setUp происходит перед каждым вызовом теста.
        """
        self.car = Car('BMW', 'x5', 2005)
        self.motorcycle = Motorcycle('Lebedev Motors', 'Ataman', 2008)

    def test_car_instance(self):
        """
        Проверить, что экземпляр объекта Car также является экземпляром транспортного средства
        """
        self.assertIsInstance(self.car, Vehicle)

    def test_num_wheels_car(self):
        """
        проверка того, объект Car создается с 4-мя колесами
        """
        self.assertEquals(self.car.num_wheels, 4)

    def test_num_wheels_motorcycle(self):
        """
        проверка того, объект Motorcycle создается с 2-мя колесами
        """
        self.assertEquals(self.motorcycle.num_wheels, 2)

    def test_num_wheels_2_car(self):
        """
        проверка того, объект Car не создается с 2-мя колесами
        """
        self.assertNotEquals(self.car.num_wheels, 2)

    def test_speed_test_drive_car(self):
        """
        проверка того, что объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
        """
        self.car.testdrive()
        self.assertEquals(self.car.get_speed(), 60)

    def test_speed_test_drive_motorcycle(self):
        """
        проверка того, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
        """
        self.motorcycle.testdrive()
        self.assertEquals(self.motorcycle.get_speed(), 75)

    def test_speed_park_car(self):
        """
        проверка того, что в режиме парковки машина останавливается (speed = 0)
        """
        self.car.testdrive()
        self.car.park()
        self.assertEquals(self.car.get_speed(), 0)

    def test_speed_park_motorcycle(self):
        """
        проверка того, что в режиме парковки мотоцикл останавливается (speed = 0)
        """
        self.motorcycle.testdrive()
        self.motorcycle.park()
        self.assertEquals(self.motorcycle.get_speed(), 0)
