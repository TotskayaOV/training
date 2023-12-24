# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

from collections import Counter

frends_dict = {'Ivan': ('вилка', 'кружка', 'спальник'),
               'Lena': ('спальник', 'пудреница', 'кружка'),
               'Denis': ('вилка', 'кружка', 'спальник')}

print(f'Все вещи, которые взяли {len(list(frends_dict.keys()))} друга: ')
values_list = [list(value) for value in frends_dict.values()]
all_things = values_list[0].copy()
for ind_list in range(1, len(values_list)):
    all_things.extend(values_list[ind_list])
first_answer = set(all_things)
for point, elem in enumerate(first_answer, 1):
    print(f'{point}. {elem}')
things_dict = Counter(thing for thing in all_things)
unic_list = []
except_list = []
for key_thing, count_thing in things_dict.items():
    if count_thing == 1:
        unic_list.append(key_thing)
    if count_thing == len(list(frends_dict.keys())) - 1:
        except_list.append(key_thing)
common_things = []
for key_names, thing_tuple in frends_dict.items():
    for elem in thing_tuple:
        if elem in unic_list:
            print(f'Только у {key_names} есть {elem}.')
            common_things = [x for x in thing_tuple if x != elem]
    if len(set(thing_tuple).union(set(except_list))) > len(thing_tuple):
        print(f"У всех друзей есть {', '.join(except_list)} кроме {key_names}.")
if common_things:
    print(f"У всех {len(list(frends_dict.keys()))} друзей есть {', '.join(common_things)}.")
