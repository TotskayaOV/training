# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
import random

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10

count = 0

guess_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
print('Василь Василич, загадал число. Угадай какое!')
while count < ATTEMPTS:
    user_input = input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: ')
    try:
        user_input = int(user_input)
        if user_input < LOWER_LIMIT or user_input > UPPER_LIMIT:
            raise Exception
    except:
        print('Нужно ввести число цифрами из указанного диапазона')
    else:
        if user_input < guess_number:
            print('Нужно выбрать число побольше')
        elif user_input > guess_number:
            print('Ну это ты перебрал! Выбери число поменьше')
        else:
            print(f'Ты угадал! Это было число {user_input}. Василь Василич салютует!')
            break
    finally:
        count += 1
        print(f'Осталось {ATTEMPTS - count} попыток')
else:
    print('Ты не готов сражаться с Василь Василичем в угадаку! Количество попыток исчерпано!')
