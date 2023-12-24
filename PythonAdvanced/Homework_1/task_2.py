# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


side_1 = float(input('Введите длину 1 стороны треугольника: '))
side_2 = float(input('Введите длину 2 стороны треугольника: '))
side_3 = float(input('Введите длину 3 стороны треугольника: '))
if side_1 + side_2 < side_3 or side_3 + side_2 < side_1 or side_1 + side_3 < side_2:
    result_string = 'Треугольника с такими сторонами не существует'
elif side_1 == side_2 == side_3:
    result_string = 'Треугольник равносторонний'
elif side_3 == side_2 != side_1 or side_1 == side_2 != side_3 or side_3 == side_1 != side_2:
    result_string = 'Треугольник равнобедренный'
else:
    result_string = f'Задан треугольник со сторонами - {side_1, side_2, side_3}'
print(result_string)


# user_input = 3
# side_list = []
# result_string = ''
# while user_input > 0:
#     side_triangle = float(input('Введите длину стороны треугольника:'))
#     side_list.append(side_triangle)
#     user_input -= 1
# for i in range(len(side_list)-1):
#     if side_list[i] == side_list[i+1]:
#         result_string = 'Треугольник равнобедренный'
# for i in range(len(side_list)):
#     check_side = sum(side_list) - side_list[i]
#     if check_side < side_list[i]:
#         result_string = 'Треугольника с такими сторонами не существует'
# if side_list[0] == side_list[1] == side_list[2]:
#         result_string = 'Треугольник равносторонний'
# print(result_string)

