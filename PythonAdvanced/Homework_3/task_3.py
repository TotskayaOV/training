# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи
# влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

itmes_dict = {'фонарик': 0.2, 'спальник': 1, 'кружка': 0.1, 'саперная лопата': 1.2, 'термобелье': 0.5,
              'котелок': 0.7, 'мясо для шашлыка': 2}
value_riukzak = 3.0
result_dict = {}

items_list = list(itmes_dict.keys())
for i in range(0, len(items_list)-1):
    val = itmes_dict.get(items_list[i])
    result_dict[str(i)+str(i+1)] = [items_list[i]]
    for j in range(i+1, len(items_list)):
        if val + itmes_dict.get(items_list[j]) < value_riukzak:
            val += itmes_dict.get(items_list[j])
            done_val = result_dict.get(str(i) + str(i + 1))
            done_val.append(items_list[j])
            result_dict[str(i) + str(i + 1)] = done_val
for i, elem in enumerate(result_dict.values()):
    print(f'{i+1}. {elem}')