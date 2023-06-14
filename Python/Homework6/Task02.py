# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 4, 5, 6]
# result_list = []
# # определяем длинну массива и, если она нечетная, округляем до большего значения, положив значение в переменную len_num
# if len(my_list)%2 > 0:
#     len_num = len(my_list)//2 + 1
# else:
#     len_num = int(len(my_list)/2) 
# # проходим до середины массива через i и добавляем в пустой массив произведения пар
# for i in range(len_num):
#     res_num = my_list[i] * my_list[len(my_list)-1-i]
#     result_list.append(res_num)
# print(result_list)


my_list = [2, 3, 4, 5, 6]
if len(my_list)%2 > 0: len_num = len(my_list)//2 + 1
else: len_num = int(len(my_list)/2) 
print([my_list[i] * my_list[len(my_list)-1-i] for i in range(len_num)])