# Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fibonachi_func(user_number):
    num_1, num_2 = 0, 1
    for _ in range(user_number):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


user_num = int(input('Введите число: '))
print(list(fibonachi_func(user_num)))
