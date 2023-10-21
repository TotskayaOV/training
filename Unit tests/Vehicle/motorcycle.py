from .vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, company: str, model: str, year_release: int):
        super().__init__(company, model, year_release)
        self._speed = 0

    @property
    def num_wheels(self):
        """
        атрибут доступный только для чтения
        """
        return 2

    def testdrive(self):
        """
        устанавливает скорость в режим тест драйв
        """
        self._speed = 75

    def park(self):
        """
        устанавливает скорость в режим парковка
        """
        self._speed = 0

    def get_company(self) -> str:
        """
        возвращает название компании
        """
        return self._company

    def get_model(self) -> str:
        """
        возвращает модель
        """
        return self._model

    def get_year_release(self) -> int:
        """
        возвращает год выпуска
        """
        return self._year_release

    def get_num_wheels(self) -> int:
        """
        возвращает количество колес
        """
        return self.num_wheels

    def get_speed(self) -> int:
        """
        возвращает текущее значение скорости
        """
        return self._speed

    def __str__(self):
        return f'This motorcycle is a {self._company} year {self._year_release} make {self._model} model.'
