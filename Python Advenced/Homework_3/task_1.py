# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть
# дубликатов.

task_list = [1, 2, 2, 3, 5, 7, 8, 9, 9, 9]
result_list = []

for item in task_list:
    if task_list.count(item) > 1 and item not in result_list:
        result_list.append(item)

print(result_list)
