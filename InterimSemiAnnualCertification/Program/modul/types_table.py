from .databases import DataBase


class TypesAnimal(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_pack_animals(self):
        sql = '''CREATE TABLE IF NOT EXISTS pack_animals 
        (id_genus INTEGER PRIMARY KEY AUTOINCREMENT, animal_genus TEXT)'''
        self.execute(sql, commit=True)

    def create_table_pet_animals(self):
        sql = '''CREATE TABLE IF NOT EXISTS pet_animals 
        (id_genus INTEGER PRIMARY KEY AUTOINCREMENT, animal_genus TEXT)'''
        self.execute(sql, commit=True)


    def add_genus(self, name_table: str, new_genus: str):
        parameters = (new_genus,)
        sql = f'''INSERT INTO {name_table}_animals (animal_genus) VALUES (?)'''
        self.execute(sql, parameters, commit=True)

    def get_all_genus(self, name_table: str):
        sql = f'''SELECT * FROM {name_table}_animals'''
        return self.execute(sql, fetchall=True)

    def get_genus(self, name_table: str, **kwargs):
        sql = f'''SELECT * FROM {name_table}_animals WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def remove_genus(self, name_table: str, **kwargs):
        sql = f'''DELETE FROM {name_table}_animals WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)