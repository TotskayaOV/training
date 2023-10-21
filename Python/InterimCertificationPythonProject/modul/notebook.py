import json
from datetime import datetime


def connection():
    try:
        with open('modul\\notebook.json', 'r') as file:
            data = json.load(file)
            return data
    except:
        with open('modul\\notebook.json', 'w') as file:
            json.dump({}, file)
            return {}


def create_note(title_note: str, note: str):
    note_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    data = {'datetime_note': note_time, 'title_note': title_note, 'note': note}
    return data


def add_notes(title_note: str, note: str):
    data = connection()
    new_data = create_note(title_note, note)
    data_keys = list(data.keys())
    if len(data_keys) == 0:
        data[1] = new_data
    else:
        index = int(data_keys[-1]) + 1
        data[index] = new_data
    close_file(data)


def close_file(data):
    with open('modul\\notebook.json', 'w') as file:
        json.dump(data, file)


def show_all_notes():
    temp_list_notes = list(connection().values())
    string_data = ''
    for i, val in enumerate(temp_list_notes, start=1):
        string_data += f"{i}. {val.get('title_note')}. {val.get('datetime_note')}\n"
    return string_data


def show_notes_date(data_obj: str):
    try:
        date_obj = datetime.strptime(data_obj, '%Y-%m-%d')
        temp_list_notes = list(connection().values())
        string_data = ''
        num_point = 1
        for i, elem in enumerate(temp_list_notes, start=1):
            temp_date = datetime.strptime(elem.get('datetime_note'), '%Y-%m-%d %H:%M')
            if temp_date.date() == date_obj.date():
                string_data += (f"{num_point}. {elem.get('title_note')}.\n"
                                f" {elem.get('datetime_note')}. Номер заметки - {i}")
                num_point += 1
        if string_data == '':
            return f'За {data_obj} заметок не найдено'
        else:
            return string_data
    except:
        return 'Ошибка ввода даты. Попробуйте еще раз'


def show_note(index):
    temp_list_notes = list(connection().values())
    string_data = temp_list_notes[index].get('title_note') + '\n'\
                  + temp_list_notes[index].get('datetime_note')\
                  + '\n' + temp_list_notes[index].get('note')
    return string_data


def change_notes(index, update_title_note, update_text):
    data = connection()
    temp_list_keys = list(data.keys())
    data[temp_list_keys[index]] = create_note(update_title_note, update_text)
    close_file(data)


def size_notebok():
    return len(list(connection().keys()))


def delete_notes(index):
    data = connection()
    del data[list(data.keys())[index]]
    close_file(data)
