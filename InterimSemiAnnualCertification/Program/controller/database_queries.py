from Program.loader import animal_db, types_db, method_dict
from .check_input import check_types, finde_type
from Program.conf import animals

def types_to_str() -> str:
    result_que = animal_db.get_all_type()
    result_str = ''
    cnt = 1
    for elem in result_que:
        result_str = result_str + f'{cnt}. {elem[1]}\n'
        cnt += 1
    return result_str

def genus_to_str(animal_type: str):
    types = check_types(animal_type)
    result_que = types_db.get_all_genus(name_table=types)
    result_str = ''
    cnt = 1
    for elem in result_que:
        result_str = result_str + f'{cnt}. {elem[1]}\n'
        cnt += 1
    return result_str

def commands_to_str(name: str, users_genus: str) -> str:
    types, genus = finde_type(users_genus)
    result_queris = method_dict.get(types).get_animal(genus, name_animal=name)
    if len(result_queris) > 0:
        if result_queris[0][3] != None:
            result_list = result_queris[0][3].split(',')
            result_string = f'Команды {name}:\n'
            for elem in result_list:
                result_string = result_string + elem + '\n'
            return result_string
        else:
            return f'{name} не знает команд'
    else:
        return 'Животное не найдено'
