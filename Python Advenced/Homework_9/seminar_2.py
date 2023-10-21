

import random as rnd


def deco(func):
    def inner(*args):
        a, b, *_ = args
        if a not in range(1, 101):
            a = rnd.randint(1, 100)
            print(f'Число не попадало в заданный диапазон! Изменено на {a}')
        if b not in range(1, 11):
            b = rnd.randint(1, 10)
            print(f'Число не попадало в заданный диапазон! Изменено на {b}')
        func(a, b)
    return inner

@deco
def guess_number(a: int, b: int):
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


if __name__ == '__main__':
    guess_number(200, 13)

