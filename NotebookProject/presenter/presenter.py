from loguru import logger
from modul import LoaderDataBase


class Presenter:

    def __init__(self, view, notebook):
        self.view = view
        self.notebook = LoaderDataBase()
        self.view.set_presenter(self)

    @logger.catch
    def is_running_db(self):
        """
        Вызывает метод проверяющий запуск Базы Данных
            :return: True - запущена, и False - ошибка запуска.
        """
        return self.notebook.load_db()

    @logger.catch
    def get_notebook(self):
        """
        :return: str возвращает строковое представление записной книжки
        """
        return self.notebook.show_all_note()

    @logger.catch
    def change_note(self, index, update_text):
        """Обновляет текст заметки в записной книжке"""
        self.notebook.change_note(index, update_text)

    @logger.catch
    def add_note(self, title_note, text_note):
        print(text_note)
        self.notebook.add_notes(title_note=title_note, text_note=text_note)


    @logger.catch
    def remove_note(self, index):
        self.notebook.remove(index)

    @logger.catch
    def get_size_notebook(self):
        """
        :return: int возвращает размер записной книжки
        """
        return self.notebook.size()

    @logger.catch
    def exit_programm(self):
        self.notebook.close_db()