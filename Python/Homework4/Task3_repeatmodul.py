# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def del_repeat(new_list):
    norepeat_list = []
    for i in new_list:
        while True:
            if i in norepeat_list:
                break
            else:
                norepeat_list.append(i)
    return norepeat_list

def main():
    my_list = [2, 1, 5, 3, 7, 2, 1, 3, 2, 9]
    my_list = del_repeat(my_list)
    print(my_list)


if __name__ == "__main__":     # точка входа
    main()


# def main():
#     user_array = []
#     result_array = []
#     user_array = list(map(int, input('Enter sequence of integer numbers. Use space bar to split. ').split()))

#     for element in user_array:
#         if user_array.count(element) == 1:
#             result_array.append(element)
#     print(f'Unique elements in array {user_array} are - ', end='')
#     print(result_array)


# if __name__ == "__main__":
#     main()


# import random
# def row_without_repeatitions(row: list) -> list:
#     sieve = {}
#     clean_row = []
#     for i in row:
#         if i in sieve:
#             sieve[i] += 1
#         else:
#             sieve.setdefault(i, 0)
#     for key, value in sieve.items():
#         if not value:
#             clean_row.append(key)

#     return clean_row


# if __name__ == '__main__':
#     row = [random.randint(1, 8) for _ in range(10)]
#     print(row)
#     print(row_without_repeatitions(row))
