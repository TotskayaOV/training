# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from Homework_9 import restarting_func,check_params,logger_json


@restarting_func(2)
@check_params
@logger_json
def guess_number(a: int, b: int) -> str:
    while b:
        user_choise = int(input('Введите свое число: '))
        if user_choise < a:
            print(f'{user_choise} меньше загаданного')
        elif user_choise > a:
            print(f'{user_choise} больше загаданного')
        else:
            return f'Ты угдал число {user_choise}'
        b -= 1
    else:
        return f'Ты не угадал число {a}'


if __name__ == '__main__':
    print(guess_number(200, 12))

