from modul import add_notes, show_all_notes, change_notes, size_notebok, delete_notes, show_notes_date, show_note


class Presenter:

    def __init__(self, view):
        self.view = view
        self.view.set_presenter(self)

    def get_notebook(self):
        """
        :return: str возвращает строковое представление записной книжки
        """
        return show_all_notes()

    def change_note(self, index, update_title_note, update_text):
        """Обновляет текст заметки в записной книжке"""
        change_notes(index, update_title_note, update_text)

    def add_note(self, title_note, text_note):
        add_notes(title_note, text_note)

    def show_note(self, index):
        return show_note(index)

    def date_note(self, date_note):
        return show_notes_date(date_note)

    def remove_note(self, index):
        delete_notes(index)

    def get_size_notebook(self):
        """
        :return: int возвращает размер записной книжки
        """
        return size_notebok()
