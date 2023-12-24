# Напишите функцию, которая принимает два целых числа (a, b, где a < b) и возвращает массив всех целых чисел между
# введеными числами, включая их.
#
# def func_code(a: int, b: int) -> list:
#     if isinstance(a, int) and isinstance(b, int):
#         return [x for x in range(a, b+1)] if a < b else []
#     else:
#         raise ValueError('Not int')

# Функция принимает число и делает его отрицательным. Ноль не имеет какого-либо математического знака.
# Если число отрицательное, тогда никаких действий не требуется. 

from fractions import Fraction

def make_negative(a):
    if isinstance(a, int | float):
        return a * (-1) if a > 0 else a
    elif isinstance(a, str):
        if '/' in a:
            try:
                return Fraction(*map(int, a.split('/'))) * (-1)
            except ValueError:
                raise ValueError('The function accepts only numbers')
        else:
            raise ValueError('The function accepts only numbers')
    else:
        raise ValueError('The function accepts only numbers')

print(make_negative('ордло'))
print(make_negative(0))