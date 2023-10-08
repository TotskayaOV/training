from block_2.easy import summarize_func
# Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той, котоая была
# решена для запуска функции суммирования.


cnt_dupl = 0
cnt_deduc = 0
cnt_div = 0


def multiplication_func(*args):
    result = 1
    for elem in args:
        result *= elem
    return result


def subtraction_func(*args):
    if len(args) == 1:
        return args
    else:
        start_num = args[0]
        for i in range(1, len(args)):
            start_num -= args[i]
        return start_num


def division_func(*args):
    if len(args) == 1:
        return args
    else:
        start_num = args[0]
        for i in range(1, len(args)):
            start_num /= args[i]
        return start_num


def team_solyanka(oper_sim='+', *args):
    match oper_sim:
        case '+': result = summarize_func(*args)
        case '-': result = subtraction_func(*args)
        case '*': result = multiplication_func(*args)
        case '/': result = division_func(*args)
        case _: result = 'Error!'
    return result


print(team_solyanka('/', 4, 2))


# Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве
# результата работы из объемлющей функции.


def total_func(*args):
    return summarize_func(*args)


result_1 = total_func(1, 2)
print(result_1)


# Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат на экран.
# Что наблюдаете?

check_func = total_func
print(check_func)   # -> <function total_func at 0x000001C2FBA60040>

# Осуществите вызов функции суммирования из полученной переменной.

print(check_func(1, 2, 3))  # -> 6
