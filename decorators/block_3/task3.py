# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
# которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
# очистки кэша в процессе выполнения функций.
# 3.3 Параметризовать время кэширования в декораторе.

from time import sleep

from datetime import datetime

cash_dict = {}


def memory_function(time_point=10):
    def outer(func):
        def inner(*args, **kwargs):
            global cash_dict
            check_value = cash_dict.get(func.__name__, False)
            current_time = datetime.now().time()
            check_args = args
            check_kwargs = kwargs
            result = True
            if check_value:
                for k in check_value.keys():
                    difference = (datetime.combine(datetime.today(), k)
                                  - datetime.combine(datetime.today(), current_time)).total_seconds()
                    if difference > time_point:
                        del check_value[k]
                for v in check_value.values():
                    if v == (check_args, check_kwargs):
                        result = False
                if result:
                    check_value[current_time] = (check_args, check_kwargs)
                    cash_dict[func.__name__] = check_value
                    return func(*args, *kwargs)
                else:
                    check_value[current_time] = (check_args, check_kwargs)
                    return None
            else:
                cash_dict[func.__name__] = {current_time: (check_args, check_kwargs)}
                return func(*args, *kwargs)
        return inner
    return outer


@memory_function(time_point=20)
def summarize_func(*args):
    return sum(args)


print(summarize_func(1, 2))
print(summarize_func(1, 2))
print(summarize_func(3, 2))
sleep(10)
print(summarize_func(1, 2))
