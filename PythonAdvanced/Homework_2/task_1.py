# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результ


DEVNUM = 16
ALPHA_DICT = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f' }
sxt_string = ''

user_number = int(input('Введите число: '))

print(f'Под капотом посчитается так: {hex(user_number)[2::]}')

while user_number:
    sxt_string = str(ALPHA_DICT.get(user_number%DEVNUM, user_number%DEVNUM)) + sxt_string
    user_number = user_number//DEVNUM

print('А у меня получается вот так: '+ sxt_string)