# Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.
# В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
# дополнительных аргументов. Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
#  * прокинуть в функцию только 1 аргумент
#  * прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу
#  * создать кортеж со значениями и распаковать его при вызове функции с помощью *
#  * создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?


def args_func1(*args):
    '''
    суммирует элементы
    :param args: digit or string
    :return: digit or string
    '''
    contains_string = any(isinstance(item, str) for item in args)
    result_string = ''
    if contains_string:
        for elem in args:
            result_string += str(elem)
        return result_string
    else:
        result = sum(args)
        return result


print(args_func1(1, 2, 3))


def args_func2(num_1, num_2, num_3, num_4, *args):
    contains_string = any(isinstance(item, str) for item in args) or type(num_1) == str or type(num_2) == str \
                      or type(num_3) == str or type(num_4) == str
    result_string = ''
    if contains_string:
        result_string = result_string + str(num_1) + str(num_2) + str(num_3) + str(num_4)
        for elem in args:
            result_string += str(elem)
        return result_string
    else:
        result = num_1 + num_2 + num_3 + num_4 + sum(args)
        return result


# print(args_func2(1)) # -> TypeError: args_func2() missing 3 required positional arguments: 'num_2', 'num_3',
#                           and 'num_4' - ошибка возникает, т.к. функция ожидает на вход минимум 4 аргумента,
#                           а получает только один
# print(args_func2(1, 2, 3, 4, num_4=4))    # -> TypeError: args_func2() got multiple values for argument 'num_4'
# print(args_func2(num_4=4, 1, 2, 3))       # -> SyntaxError: positional argument follows keyword argument
print(args_func2(num_4=4, num_1=1, num_3=3, num_2=2))    # если передавать аргументы только по ключам, то можно передавать
                                                         # их в произвольном порядке, но в случае передачи без ключа
                                                         # аргументы должны располгататься на своих местах, т.к. функция
                                                          # будет присваивать их своим внутренним переменным поочередно
args_tuple = (1, 2, 3, 4)
print(args_func2(*args_tuple))
args_dict = {'num_1': 1, 'num_2': 2, 'num_3': 3, 'num_4': 4}
print(args_func2(*args_dict))   # -> num_1num_2num_3num_4
print(args_func2(**args_dict))  # -> 10
# В случае передачи словаря с * в функцию передаются только ключи. С ** - передаются пары ключ=значение
