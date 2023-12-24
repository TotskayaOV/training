# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle

PATH_FILE = './two_file.pickle'
PATH_CSV = './two_file.csv'

def reade_pickle_file(path):
    with open(path, 'rb') as file:
        new_dict = pickle.load(file)
    return new_dict

def create_csv_table(data: dict):
    csv_headers = list(data.keys())
    csv_table  = list(data.values())
    csv_table = list(zip(*csv_table))
    with open(PATH_CSV, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, dialect='excel', delimiter=' ', )
        file_writer.writerow(csv_headers)
        file_writer.writerows(csv_table)


def create_krivoi_csv(data: dict):
    csv_headers = list(data.keys())
    csv_table = list(data.values())
    csv_table = list(zip(*csv_table))
    with open(PATH_CSV, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter=",",
                                     lineterminator="\r", fieldnames=csv_headers)
        file_writer.writeheader()
        for elem in csv_headers:
            file_writer.writerow(data)


if __name__ == '__main__':
    create_csv_table(reade_pickle_file(PATH_FILE))
