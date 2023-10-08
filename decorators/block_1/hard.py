# Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы,
# первые 2 аргумента из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов
# (если они есть), переданных по ключу (если они есть).


def summarize_func(num_1, num_2, *, num_3=0, num_4=0):
    result = num_1 + num_2
    if num_3:
        result += num_3
        return result
    elif num_4:
        result += num_4
        return result
    else:
        return result


print(summarize_func(1, 2))  # -> 3
print(summarize_func(1, 2, num_3=3))    # 6
print(summarize_func(1, 2, num_3=3, num_4=4))    # -> 6
print(summarize_func(1, 2, num_4=4))     # -> 7
# print(summarize_func2(1, 2, 3)) # -> TypeError: summarize_func2() takes 2 positional arguments but 3 were given
