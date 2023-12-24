# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.

user_number = int(input('Введите положительное число меньше 100 000: '))
check_prime = True
if 100001 < user_number or user_number < 0:
    result_str = 'Введенное число не входит в заданный диапазон'
    check_prime = False
else:
    for i in range(2, user_number // 2 + 1):
        if user_number % i == 0:
            result_str = f'Число {user_number} не вляется простым'
            check_prime = False
            break
if check_prime is True:
    result_str = f'Число {user_number} является простым'
print(result_str)