from pyxll import xl_func

@xl_func
def any_number(num1, num2):
    try:
        if num1 < num2:
            if num2 < 0:
                return (num1-num2) * (-1)
            else:
                if num1 < 0:
                    return num2 + (num1 *(-1))
                else:
                    return num2 - num1
        else:
            if num1 < 0:
                return (num2-num1) * (-1)
            else:
                if num2 < 0:
                    return num1 + (num2 *(-1))
                else:
                    return num1 - num2

    except:
        return 'Ошибка ввода данных. Введите число'
