# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в  файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
# и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle


def get_directory_size(path: str) -> int:
    total_size = 0
    for root, directory, files in os.walk(path):
        for file in files:
            fp = os.path.join(root, file)
            total_size += os.path.getsize(fp)
    return total_size


def get_objects_info(path: str) -> list:
    result_list = []
    for root, directory, files in os.walk(path):
        for dir in directory:
            dir_info = {"name": dir,
                        "parent_directory": root,
                        "is_directory": True,
                        "size": get_directory_size(os.path.join(root, dir))}
            result_list.append(dir_info)
        for file in files:
            file_info = {"name": file,
                         "parent_directory": root,
                         "is_directory": False,
                         "size": os.path.getsize(os.path.join(root, file))}
            result_list.append(file_info)
    return result_list


def save_to_json(info_lst: list, output_file: str = "directory_contents.json"):
    with open(output_file, "w") as json_file:
        json.dump(info_lst, json_file, indent=4, ensure_ascii=False)


def save_to_csv(info_lst: list, output_file: str = "directory_contents.csv"):
    with open(output_file, "w", newline="") as csv_file:
        fieldnames = ["name", "parent_directory", "is_directory", "size"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(info_lst)


def save_to_pickle(info_lst: list, output_file: str = "directory_contents.pickle"):
    with open(output_file, "wb") as pickle_file:
        pickle.dump(info_lst, pickle_file)


def directory_recursion(input_directory):
    info_list = get_objects_info(input_directory)
    save_to_json(info_list)
    save_to_csv(info_list)
    save_to_pickle(info_list)


if __name__ == '__main__':
    directory_recursion("./..")
