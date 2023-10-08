# Написать простую функцию, которая на вход принимает строку ('test') и целое число (3), а возвращает строку вида
# 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
# Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
# Вызвать функцию суммирования через переменную, в которую вы только что её записали.

def multiplication_func(user_word: str, user_number: int) -> str:
    cnt = 1
    result_string = ''
    while cnt < user_number + 1:
        if cnt % 2 != 0:
            result_string += user_word.lower()
            cnt += 1
        else:
            result_string += user_word.upper()
            cnt += 1
    return result_string


user_word = 'test'
user_number = 3
print(multiplication_func(user_word, user_number))  # -> testTESTtest
arbitrary_variable = multiplication_func
print(arbitrary_variable)                           # <function cube_func at 0x00000187EDDAF010>
print(arbitrary_variable(user_word, user_number))   # -> testTESTtest
