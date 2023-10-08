# Задача 1

# 1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать
# в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.


def cats(func):
    def inner_func(*args, **kwargs):
        print('Покупайте наших котиков!')
        return func(*args, **kwargs)
    return inner_func


@cats
def summarize_func(*args):
    return sum(args)

# result_funk = cats(summarize_func)
print(summarize_func(1, 2))


# 1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
# как параметр во время декорирования.


def new_cats(text='Покупайте наших котиков!'):
    def new_text(func):
        def inner(*args, **kwargs):
            print(text)
            return func(*args, **kwargs)
        return inner
    return new_text


@new_cats(text='Покупайте наших котиков, они клёвые!')
def summarize_func2(*args):
    return sum(args)


print(summarize_func2(1, 2))
