from .control import Control
from .menu import Menu
from .view import View


class Console(View):
    """Класс реализует взаимодействие с пользователем"""
    working = True
    open = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def show_all(self):
        """
        :return: Вывод всех заметок в консоль или сообщение об ошибке
        """
        print(self.presenter.get_notebook())

    def show_date(self):
        """
            Показать заметку за определенную дату
        :return: str
        """
        date_note = input("\nВведите дату в формате YYYY-MM-DD: ")
        print(self.presenter.date_note(date_note))

    def show_note(self):
        """
        Показать заметку по номеру
        :return: int индекс заметки
        """
        index = Control.get_index(self.presenter.get_size_notebook(), "\nВведите номер заметки: ")
        print(self.presenter.show_note(index))

    def remove_note(self):
        """
             Удаление заметки по номеру
        :return: int индекс заметки
        """
        index = Control.get_index(self.presenter.get_size_notebook(), "\nВведите номер заметки: ")
        self.presenter.remove_note(index)
        print("\nЗаметка удалена.")

    def change_note(self):
        """
            Изменения заметки по номеру
        :return: int индекс заметки
        """
        index = Control.get_index(self.presenter.get_size_notebook(), "\nВведите номер заметки: ")
        update_title_note = input("\nОбновите название заметки: ")
        update_note = input("\nОбновите заметку: ")
        self.presenter.change_note(index, update_title_note, update_note)
        print("\nЗаметка изменена.")

    def add_note(self):
        """
            Добавления новой заметки
        :return: str текст заметки
        """
        new_title = input("\nВведите название заметки: ")
        new_note = input("\nВведите заметку: ")
        self.presenter.add_note(new_title, new_note)
        print("\nЗаметка добавлена.")

    def finish(self):
        self.working = False
        print("\nЗавершение работы...")

    def start(self):
        self.working = True
        menu = Menu(self)
        while self.working:
            print(menu)
            index = Control.get_index(menu.get_size_menu(), "\nВыберите пункт меню: ")
            menu.execute(index)
