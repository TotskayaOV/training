# Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код? Если да, то как поменялся
# смысл написанного кода? Если нет, то что надо изменить, чтобы всё заработало?

cnt = 0


def total_func(*args):
    global cnt

    def summarize_func(cnt, *args):
        cnt += 1
        return (cnt, sum(args))
    result = summarize_func(cnt, *args)
    cnt = result[0]
    return result[1]


print(total_func(1, 2))
print(cnt)

# Если не передать summarize_func cnt в качестве аргумента, то программа вылетит с ошибкой:
# UnboundLocalError: local variable 'cnt' referenced before assignment, чтобы этого не происходило, глобальную
# переменную нужно передавать в качестве аргумента внутри функции total_func или определять в качестве глобальной уже
# внутри функции summarize_func
