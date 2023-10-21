# Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.

def simple_generic(stop_num) -> int:
    temp_list = []
    for i in range(2, stop_num + 1):
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            yield i

user_input = int(input('N=: '))
print(list(simple_generic(user_input)))
