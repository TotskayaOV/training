# Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.

cnt = 0


def summarize_func(*args):
    global cnt
    cnt += 1
    return sum(args)


print(cnt)  # -> 0
result_1 = summarize_func(1, 2)
result_2 = summarize_func(1, 2)
result_3 = summarize_func(1, 2)
print(cnt)  # -> 3
