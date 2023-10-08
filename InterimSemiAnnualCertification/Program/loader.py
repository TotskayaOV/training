from modul import DataBase, Animals, TypesAnimal, PackAnimal, PetAnimal, Counter

db = DataBase(db_path='./db_nursery.db')
animal_db = Animals()
types_db = TypesAnimal()
pack_db = PackAnimal()
pet_db = PetAnimal()
counter = Counter()
method_dict = {'pet': pet_db, 'pack': pack_db}


def on_startup():
    try:
        animal_db.create_table_animals()
        types_db.create_table_pet_animals()
        types_db.create_table_pack_animals()
        pack_db.create_table_horses()
        pack_db.create_table_donkeys()
        pack_db.create_table_camels()
        pet_db.create_table_dogs()
        pet_db.create_table_cats()
        pet_db.create_table_hamsters()
        if len(animal_db.get_type(id=1)) == 0: animal_db.add_type('pack')
        if len(animal_db.get_type(id=2)) == 0: animal_db.add_type('pet')
        if len(types_db.get_genus(name_table='pack', animal_genus='horses')) == 0:
            types_db.add_genus(name_table='pack', new_genus='horses')
        if len(types_db.get_genus(name_table='pack', animal_genus='donkeys')) == 0:
            types_db.add_genus(name_table='pack', new_genus='donkeys')
        if len(types_db.get_genus(name_table='pack', animal_genus='camels')) == 0:
            types_db.add_genus(name_table='pack', new_genus='camels')
        if len(types_db.get_genus(name_table='pet', animal_genus='dogs')) == 0:
            types_db.add_genus(name_table='pet', new_genus='dogs')
        if len(types_db.get_genus(name_table='pet', animal_genus='cats')) == 0:
            types_db.add_genus(name_table='pet', new_genus='cats')
        if len(types_db.get_genus(name_table='pet', animal_genus='hamsters')) == 0:
            types_db.add_genus(name_table='pet', new_genus='hamsters')
    except Exception as err:
        print(f'Error DB\n{err}')
    else:
        print('DataBase...done!')