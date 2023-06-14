# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# Number = input("Введите вещественное число: ")
# sum1 = 0
# for i in Number:
#     if i.isdigit():
#         sum1 += int(i)
# print(sum1)

user_number = input("Введите вещественное число: ")
result = list(map(int, filter(lambda i: i.isdigit(), user_number)))
print(sum(result))