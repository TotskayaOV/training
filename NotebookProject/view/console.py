from loguru import logger

from .control import Control
from .menu import Menu
from .view import View

class Console(View):
    """Класс реализует взаимодействие с пользователем"""
    working = False
    open = False


    def __init__(self):
        self.presenter = None


    @logger.catch
    def set_presenter(self, presenter):
        self.presenter = presenter

    @logger.catch
    def show_all(self):
        """
        :return: Вывод всех заметок в консоль или сообщение об ошибке
        """
        if self.presenter.is_running_db():
            print(self.presenter.get_notebook())
        else:
            print("\nОшибка: Отсутствует подключение к Базе Данных")

    @logger.catch
    def remove_note(self):
        """
             Удаление заметки по номеру
        :return: int индекс заметки
        """
        if self.presenter.is_running_db():
            index = Control.get_index(self.presenter.get_size_notebook(), "\nВведите номер заметки: ")
            self.presenter.remove_note(index)
            print("\nЗаметка удалена.")
        else:
            print("\nОшибка: Отсутствует подключение к Базе Данных")

    @logger.catch
    def change_note(self):
        """
            Изменения заметки по номеру
        :return: int индекс заметки
        """
        if self.presenter.is_running_db():
            index = Control.get_index(self.presenter.get_size_notebook(), "\nВведите номер заметки: ")
            update_note = input("\nОбновите заметку: ")
            self.presenter.change_note(index, update_note)
            print("\nЗаметка изменена.")
        else:
            print("\nОшибка: Отсутствует подключение к Базе Данных")

    @logger.catch
    def add_note(self):
        """
            Добавления новой заметки
        :return: str текст заметки
        """
        if self.presenter.is_running_db():
            new_title = input("\nВведите название заметки: ")
            new_note = input("\nВведите заметку: ")
            self.presenter.add_note(new_title, new_note)
            print("\nЗаметка добавлена.")
        else:
            print('\nОшибка: Отсутствует подключение к Базе Данных')

    @logger.catch
    def finish(self):
        self.presenter.exit_programm()
        self.working = False
        print("\nЗавершение работы...")

    @logger.catch
    def start(self):
        self.working = True
        menu = Menu(self)
        while self.working:
            print(menu)
            index = Control.get_index(menu.get_size_menu(), "\nВыберите пункт меню: ")
            menu.execute(index)