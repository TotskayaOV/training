# 📌Создайте декоратор с параметром.
# 📌Параметр - целое число, количество запусков декорируемой функции.


from typing import Callable

def restarting_func(cnt: int):
    def outer(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            result = []
            for _ in range(cnt):
                result.append(func(*args, *kwargs))
            return result
        return inner
    return outer
