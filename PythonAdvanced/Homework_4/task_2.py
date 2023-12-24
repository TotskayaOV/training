# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного
# аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def my_func(**kwargs):
    result = {}
    for key, arg in kwargs.items():
        if not isinstance(arg, (int, float, str, tuple, frozenset)):
            arg = str(arg)
        result[arg] = key
    return result


print(my_func(a=1, b=[1, 2, 3], c=(2, 3), d='s', e=0.2, f={1, 2}))
