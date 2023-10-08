from Program.conf import pet_animal, pack_animal, animals


def check_types(users_types):
    if users_types.lower() in pet_animal:
        types = pet_animal[0]
    if users_types.lower() in pack_animal:
        types = pack_animal[0]
    return types


def check_genus(types: str, users_genus: str) -> str:
    for values in animals.get(types):
        if users_genus.lower() in values:
            return values[0]

def finde_type(users_genus: str) -> tuple:
    for typ_an, values in animals.items():
        for gen_an in values:
            if users_genus in gen_an:
                types = typ_an
                genus = gen_an[0]
    return (types, genus)
