from Program.loader import animal_db, types_db, pet_db, pack_db, method_dict
from Program.conf import animals
from .check_input import check_types, finde_type


def adding_new_animal(new_data: dict) -> str:
    type_animal = new_data.get('type')
    type_animal = check_types(type_animal)
    for values in animals.get(type_animal):
        if new_data.get('genus') in values:
            genus_animal = values[0]
    method_dict.get(type_animal).add_animal(name_table=genus_animal,
                       new_data={'name': new_data.get('name'),
                                 'birthday': new_data.get('birthday'),
                                 'genus_id': types_db.get_genus(name_table=type_animal,
                                                                animal_genus=genus_animal)[0][0]})
    return 'Животное добавлено в реестр Пиомника'


def add_new_commands(name_animal: str, genus_animal: str, animal_command: str) -> str:
    types, genus = finde_type(genus_animal)
    result_queris = method_dict.get(types).get_animal(genus, name_animal=name_animal)
    if len(result_queris) > 0:
        if result_queris[0][3] != None:
            commands_string = result_queris[0][3] + f', {animal_command}'
            method_dict.get(types).update_animal(genus, 'commands_animal',
                                                 {'id': result_queris[0][0], 'value': commands_string})
        else:
            method_dict.get(types).update_animal(genus, 'commands_animal',
                                                 {'id': result_queris[0][0], 'value': animal_command})
        return 'Команда добавлена'
    else:
        return f'Животное по кличке {name_animal} не найдено'
