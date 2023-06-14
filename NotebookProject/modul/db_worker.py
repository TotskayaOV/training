import sqlite3
from datetime import datetime
from loguru import logger
from config import db_path

from .notebook import JsonNoteFile as db
from .note import Note

class LoaderDataBase:
    def __init__(self, json_path: str = 'modul/notebook_db.json'):
        self.js_path = json_path
        self.db = db()

    @logger.catch
    def load_db(self):
        # self.db = db(json_path='modul/notebook_db.json')
        try:
            self.db.connection()
            # print('DataBase...ok!')
            return True
        except:
            self.db.create_notebook()
        finally:
            return True

    @logger.catch
    def data_conversion(self):
        """
        Метод преобразует данные полученные из Базы данных в два списка для корректного отображения.
        Первый список содержит id заметок, второй сами заметки. Таким образом возможно обращение к
        конкретной заметке в Базе Данных по ее id  при том, что пользователь будет вводить номер заметки
        не имеющий ничего общего с ее id. МОжно использовать при работе с другими формами хранения данных,
        например gson файлы.
        :return: list [list[id], list[Note]]
        """
        temp_list = self.db.show_all_notes()
        index_list = []
        notes_list = []
        for i in range(len(temp_list)):
            index_list.append(temp_list[i][0])
            note = Note(temp_list[i][1], temp_list[i][2])
            notes_list.append(note)
        all_list = [index_list, notes_list]
        return all_list

    @logger.catch
    def add_notes(self, title_note: str, text_note: str):
        note_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        temp_dict = Note(note_time, title_note, text_note)
        self.db.add_note_from_db(notes=temp_dict.get())

    @logger.catch
    def change_note(self, index, new_text):
        """
        Изменяет заметку делая запрос в Базу данных по id. Поиск id происходит по индексу в 1
        списке списков
        :param index: int индекс id
        :param new_text: str текст новой заметки
        :return:
        """
        note_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        temp_list = self.data_conversion()
        self.db.update_notes(notes={'date_created': note_time, 'note': new_text, 'id': temp_list[0][index]})

    @logger.catch
    def show_all_note(self):
        temp_list = self.data_conversion()
        notes_string = "\nСписок заметок:\n"
        for i, note in enumerate(temp_list[1], start=1):
            notes_string += f"\t{i}. {note}\n"
        return notes_string

    @logger.catch
    def remove(self, index: int):
        temp_list = self.data_conversion()
        id_note = temp_list[0][index]
        self.db.remove_notes(id_note)

    @logger.catch
    def size(self):
        temp_list = self.data_conversion()
        return len(temp_list[0])

    @logger.catch
    def close_db(self):
        self.db.disconnect()







