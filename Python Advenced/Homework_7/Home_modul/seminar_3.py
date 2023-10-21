# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более кор

def combining_func():
    data_1 = []
    with open('text_seminar.txt', 'r', encoding='UTF-8') as file_1:
        data_1 = file_1.readlines()

    data_2 = []
    with open('name_seminar.txt', 'r', encoding='UTF-8') as file_2:
        data_2 = file_2.readlines()

    with open('task_3_file.txt', 'a+', encoding='UTF-8') as file_3:
        data_3 = []
        max_size = max(len(data_1), len(data_2))
        min_size = min(len(data_1), len(data_2))

        for i in range(max_size):
            a, b = data_1[i % min_size].split(' | ')
            mul = int(a) * float(b)
            if mul < 0:
                data_3.append(f'{data_2[i % min_size].lower().strip()} | {abs(mul)}')
            else:
                data_3.append(f'{data_2[i % min_size].upper().strip()} | {int(mul)}')

        file_3.write('\n'.join(data_3))


if __name__ == '__main__':
    combining_func()
