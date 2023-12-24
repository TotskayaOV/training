# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.


import math
import random as rnd
import csv
import json
import os
from typing import Callable


UPPER_LIMIT = 100
PATH_FILE = 'new_file.csv'


def logger_json(func: Callable) -> Callable:
    """
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
    {параметры: результат}
    """
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        data = {}
        if os.path.isfile(file_name) and os.path.exists(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        result = func(*args, **kwargs)
        first_step, two_step = '', ''
        if args:
            firs_step = ' '.join(list(map(str, args)))
        if kwargs:
            two_step = [f'{k}-{v}' for k, v in kwargs.items()]
        data[firs_step + two_step] = result
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return result
    return wrapper



@logger_json
def find_roots(a, b, c):
    """
    функция нахождения корней квадратного уравнения
    """
    if a == 0:
        return ('Некорректное значение')
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))
    if dis_form > 0:
        return ((-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a))
    elif dis_form == 0:
        return (-b / (2 * a),)
    else:
        return (f'{- b / (2 * a)}+ i{sqrt_val}', f'{- b / (2 * a)}- i{sqrt_val}')


def generic_csv_file(path : str = PATH_FILE):
    """
    Генерация csv файла с тремя случайными числами в каждой строке
    """
    data_list = [(rnd.randint(0, 20) for _ in range(3)) for _ in range(UPPER_LIMIT)]
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)


def strange_decorator(func: Callable) -> Callable:
    """
    декоратор запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    """
    def inner(*args, **kwargs):
        if os.path.isfile(PATH_FILE) and os.path.exists(PATH_FILE):
            with open(PATH_FILE, 'r', encoding='UTF-8') as file:
                data = file.readlines()
            for elem in data:
                result = find_roots(*list(map(int, elem.rstrip().split(','))))
        return func(*args, **kwargs)
    return inner


@strange_decorator
def summaraze(a, b):
    """
    Функци для демонстрации работы декоратора
    """
    return a + b


if __name__ == '__main__':
    generic_csv_file()
    summaraze(1, 2)
