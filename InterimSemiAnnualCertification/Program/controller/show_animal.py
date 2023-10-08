from Program.loader import method_dict
from Program.conf import animals
from .check_input import check_types, check_genus



def genus_animals_to_string(types: str, genus: str) -> str:
    result_string = ''
    result_list = method_dict.get(types).get_all_animal(genus)
    for elem in result_list:
        result_string += f"{elem[1]} (дата рождения: {elem[2]})\n"
    return result_string


def types_animals_to_string(types: str) -> str:
    result_string = ''
    list_genus = animals.get(types)
    for elem in list_genus:
        result_string += elem[2].title() + ':\n' + genus_animals_to_string(types, elem[0])
    return result_string


def show_animals(types=False, genus=False) -> str:
    if genus:
        types = check_types(types)
        genus = check_genus(types, genus)
        return genus_animals_to_string(types, genus)
    else:
        if types:
            types = check_types(types)
            return types_animals_to_string(types)
        else:
            result_string = ''
            for keys in animals.keys():
                types = check_types(keys)
                if types_animals_to_string(types):
                    result_string += types_animals_to_string(types)
            return result_string
