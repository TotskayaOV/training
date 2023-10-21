from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
        Абстрактный базовый класс для всех видов транспортных средств
        Атрибут:
        ABC (класс): класс ABC из модуля abc, необходимый для создания абстрактных классов."""

    def __init__(self, company: str, model: str, year_release: int):
        self._company = company
        self._model = model
        self._year_release = year_release
        self._speed = 0

    @property
    def _num_wheels(self):
        return 0

    @abstractmethod
    def testdrive(self):
        """Aбстрактный метод"""

    @abstractmethod
    def park(self):
        """Aбстрактный метод"""
