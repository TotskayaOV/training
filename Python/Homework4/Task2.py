# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import Task3_repeatmodul

num = int(input("Введите число: "))
i = 2  
my_list = []
temp = num
while i <= num:
    if num % i == 0:
        my_list.append(i)
        num //= i
        i = 2
    else:
        i += 1

print(f"Список простых множителей числа {temp}: {Task3_repeatmodul.del_repeat(my_list)}")


# def sieve_of_eratosthenes(number: int) -> list:
#     row = {i: '_' for i in range(2, number + 1) if i == 2 or i > 2 and i % 2 != 0}
#     # use a dict cause a list too expensive operation for deletion items
#     i = 2
#     while True:
#         if i ** 2 > number:
#             break
#         elif i != 2 and i % 2 == 0:
#             i += 1
#             continue

#         for j in range(i, number + 1, 2):
#             if j * i > number:
#                 break
#             elif (j * i) in row:
#                 del row[j * i]
#         i += 1
#     return list(row)


# def prime_factorization(number: int) -> list:
#     prime_numbers = sieve_of_eratosthenes(number)
#     if number in prime_numbers: return [number]
#     prime_factors = [i for i in prime_numbers if number % i == 0]
#     return prime_factors


# if __name__ == '__main__':
#     print(prime_factorization(2200))
#     print(prime_factorization(239))
#     print(prime_factorization(100))



# from random import randint

# def prime_factors(temp: int) -> list:
#     result = []
#     while temp > 1:
#         for i in range(2, int(temp ** 0.5) + 1):
#             if not temp % i:
#                 temp //= i
#                 if not i in result:
#                     result.append(i)
#                 break
#         else: 
#             # if not (temp in result):
#             result.append(temp)
#             temp = 1
#     return result


# def main():
#     number = 1123
#     print(f'Простые множители числа {number}: {prime_factors(number)}')


# if __name__ == '__main__':
#     main()
