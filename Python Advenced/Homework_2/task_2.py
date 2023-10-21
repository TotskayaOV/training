# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def search_max_div(full_number: int) -> list:
    """
    Функция находит все делители числа, кроме 1 и самого числа
    :param full_number:  int
    :return: list
    """
    div_list = []
    for i in range(2, int(full_number // 2 + 1)):
        if full_number % i == 0:
            div_list.append(i)
    return map(int, div_list)

def converting_to_number(num_str: str) -> (int, int):
    """
    Конвертирует строковое представление дроби в два числа: числитель и знаменатель
    :param num_str: str
    :return: tuple
    """
    return tuple(map(int, num_str.split('/')))

def converting_to_string(numerator, denominator) -> str:
    """
    Проверяет можно ли сократить дробь, выделить целое
    :param numerator: числитель
    :param denominator: знаменатель
    :return: строковое представление дроби
    """
    div_denominators = search_max_div(denominator)
    div_numerators = search_max_div(numerator)
    div_res = set(div_denominators).intersection(set(div_numerators))
    if div_res:
        max_div = list(div_res)[0]
        for elem in div_res:
            if elem > max_div:
                max_div = elem
        numerator /= max_div
        denominator /= max_div
    if numerator > denominator:
        ful_num = int(numerator // denominator)
        if numerator % denominator == 0:
            result_string = str(ful_num)
        else:
            result_string = f'{ful_num} {int(numerator % denominator)}/{int(denominator)}'
    else:
        result_string = f'{int(numerator)}/{int(denominator)} '
    return result_string

def converting_equation_to_string(num_1, num_2, num_3, num_4) -> str:
    """
    Строковое представление уравнений
    :param num_1: первая переменная
    :param num_2: вторая переменная
    :param num_3: результат сложения
    :param num_4: результат умножения
    :return: str
    """
    return f'{num_1} + {num_2} = {num_3}\n{num_1} * {num_2} = {num_4}'


first_user_string = input('Введите первую дробь: ')
two_user_string = input('Введите вторую дробь: ')
numerator_1, denominator_1 = converting_to_number(first_user_string)
numerator_2, denominator_2 = converting_to_number(two_user_string)

fr_1 = Fraction(numerator_1, denominator_1)
fr_2 = Fraction(numerator_2, denominator_2)

if denominator_1 == 0 or denominator_2 == 0:
    total_result = 'У дроби с делителем равным 0 нет значения'
elif numerator_1 == 0 or numerator_2 == 0:
    if numerator_2 != 0:
        total_result = converting_equation_to_string(first_user_string, two_user_string, two_user_string, 0)
    elif numerator_1 != 0:
        total_result = converting_equation_to_string(first_user_string, two_user_string, first_user_string, 0)
    else:
        total_result = converting_equation_to_string(first_user_string, two_user_string, 0, 0)
else:
    result_mult = converting_to_string((numerator_1 * numerator_2), (denominator_1 * denominator_2))
    if denominator_1 == denominator_2:
        numerator_sum = int(numerator_2 + numerator_1)
        noz = denominator_1
    else:
        # ищем наименьший общий знаменатель
        div_list1 = search_max_div(denominator_1)
        div_list2 = search_max_div(denominator_2)
        div_denominators = set(div_list1).intersection(set(div_list2))
        if len(div_denominators) == 0:
            noz = denominator_1 * denominator_2
        else:
            max_div = list(div_denominators)[0]
            for elem in div_denominators:
                if elem > max_div:
                    max_div = elem
            noz = int(denominator_1 * denominator_2 / max_div)
        numerator_1 = noz / denominator_1 * numerator_1
        numerator_2 = noz / denominator_2 * numerator_2
        numerator_sum = int(numerator_2 + numerator_1)
    result_sum = converting_to_string(numerator_sum, noz)
    total_result = converting_equation_to_string(first_user_string, two_user_string, result_sum, result_mult)

print(f'Результат:\n{total_result}')
print(f'Проверка:\nСумма: {fr_1 + fr_2}\nПроизведение: {fr_1 * fr_2}')