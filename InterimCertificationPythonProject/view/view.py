from abc import ABC, abstractmethod


class View(ABC):
    """
        Абстрактный базовый классо для всех классов представлений (Views) в приложении.
    """

    @abstractmethod
    def set_presenter(self, presenter):
        """
            Принимает экземпляр класса Presenter в качестве аргумента.
        """

    @abstractmethod
    def start(self):
        """
            Выполняет начальную настройку представления и запускет его отображение.
        """
