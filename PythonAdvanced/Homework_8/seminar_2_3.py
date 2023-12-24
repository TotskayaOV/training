# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌После каждого ввода добавляйте новую информацию в JSON файл.
# 📌Пользователи группируются по уровню доступа.
# 📌Идентификатор пользователя выступает ключём для имени.
# 📌Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌При перезапуске функции уже записанные в файл данные должны сохраняться.

import os
import json
import csv

UPPER_LVL = 7
LOWER_LVL = 1
PATH_DB = './first_file.json'
PATH_CSV = './first_file.csv'

def input_name() -> str:
    user_input_name = input('Введите имя или введите exit для выхода из программы: ')
    if user_input_name == 'exit':
        exit()
    return user_input_name

def input_id_user(id_list) -> int:
    while True:
        user_input_id = input('Введите id пользователя: ')
        if user_input_id in id_list:
            print('Такой id уже существует')
        else:
            return user_input_id

def input_level_access() -> int:
    while True:
        user_input_level = input('Введите уровень доступа: ')
        if user_input_level.isdigit():
            if LOWER_LVL - 1 < int(user_input_level) < UPPER_LVL + 1:
                return int(user_input_level)
            else:
                continue
        else:
            continue

def load_file() -> dict:
    if os.path.exists(PATH_DB):
        with open(PATH_DB, 'r', encoding='UTF-8') as f:
            return json.load(f)
    else:
        return {}

def write_file(json_dict):
    with open(PATH_DB, 'w', encoding='UTF-8') as f:
        json.dump(json_dict, f, indent=4, ensure_ascii=False)

def convertation_json_to_csv():
    with (
        open(PATH_DB, 'r', encoding='UTF-8') as file_json,
        open(PATH_CSV, 'w+', encoding='UTF-8') as file_csv
    ):
        read_json = json.load(file_json)
        csv_writer = csv.writer(file_csv, delimiter=",", lineterminator="\r")
        csv_writer.writerow("ID", "Имя", "Уровень доступа")
        for lvl, values in read_json.items():
            for id_u, name in values.items():
                csv_writer.writerow([id_u, name, lvl])


def write_new_user():
    json_dict = load_file()
    if json_dict:
        id_list = [key for elem in list(json_dict.values()) for key, values in elem.items()]
    else:
        id_list = []
    name = input_name()
    id_u = input_id_user(id_list)
    level_access = input_level_access()
    lvl_dict = json_dict.get(str(level_access), {})
    lvl_dict[id_u] = name
    json_dict[str(level_access)] = lvl_dict
    write_file(json_dict)




if __name__ == '__main__':
    while True:
        write_new_user()
        convertation_json_to_csv()
