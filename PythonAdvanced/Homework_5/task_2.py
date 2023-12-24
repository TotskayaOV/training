# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os.path


def path_func(in_str: str):
    first_step = os.path.split(in_str)
    two_step = first_step[1].split('.')
    return (first_step[0], *two_step)

print(path_func("C:/Users/ASUS/Documents/python/main.py"))
