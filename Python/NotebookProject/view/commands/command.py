from abc import ABC, abstractmethod


class Command(ABC):
    """
        Абстрактный базовый класс для всех команд
        Атрибут:
        ABC (класс): класс ABC из модуля abc, необходимый для создания абстрактных классов."""

    @abstractmethod
    def description(self):
        """Aбстрактный метод, который должен возвращать описание команды."""

    @abstractmethod
    def execute(self):
        """Aбстрактный метод, который должен выполнять действия, связанные с выполнением команды."""