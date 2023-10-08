# 2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае
# успешного выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение
# функции было повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию
# так и не удастся выполнить успешно, то бросать исключение.


def check_docrator(func):
        def inner(*args, **kwargs):
            check_point = 0
            while check_point < 10:
                print(f'{check_point + 1} попытка')
                try:
                    return func(*args, **kwargs)
                except:
                    check_point += 1
            return 'Error!'
        return inner


@check_docrator
def summarize_func(*args):
    return sum(args)


print(summarize_func(1, 'one'))

# 2.2 Параметризовать декоратор таким образом, чтобы # количество попыток выполнения функции можно было задавать
# как параметр во время декорирования.


def new_check_docrator(check_number=0):
    def outer(func):
        def inner(*args, **kwargs):
            check_point = 0
            while check_point < check_number:
                print(f'{check_point + 1} попытка')
                try:
                    return func(*args, **kwargs)
                except:
                    check_point += 1
            return 'Error!'
        return inner
    return outer


@new_check_docrator(check_number=5)
def summarize_func2(*args):
    return sum(args)


print(summarize_func2(1, 'one'))
