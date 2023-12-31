# 📌Создайте функцию-замыкание, которая запрашивает два целых числа: ○ от 1 до 100 для загадывания, ○
# от 1 до 10 для количества попыток
# 📌Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
# 📌Дорабатываем задачу
# 1. 📌Превратите внешнюю функцию в декоратор.
# 📌Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# 📌Если не входят, вызывать функцию со случайными числами из диапазонов.

import random as rnd

def outer():
    a = rnd.randint(1, 100)
    b = rnd.randint(1, 10)
    def guess_number():
        nonlocal a, b
        while b:
            user_choise = int(input('Введите свое число: '))
            if user_choise < a:
                print(f'{user_choise} меньше загаданного')
            elif user_choise > a:
                print(f'{user_choise} больше загаданного')
            else:
                print(f'Ты угдал число {user_choise}')
                break
            b -=1
        else:
            print(f'Ты не угадал число {a}')
    return guess_number

if __name__ == '__main__':
    outer()