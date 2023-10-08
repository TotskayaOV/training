from .databases import DataBase


class PetAnimal(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_dogs(self):
        sql = '''CREATE TABLE IF NOT EXISTS dogs 
        (id_animal INTEGER PRIMARY KEY AUTOINCREMENT, name_animal TEXT,
        birthday_animal DATE, commands_animal TEXT, genus_id INTEGER)'''
        self.execute(sql, commit=True)

    def create_table_cats(self):
        sql = '''CREATE TABLE IF NOT EXISTS cats 
        (id_animal INTEGER PRIMARY KEY AUTOINCREMENT, name_animal TEXT,
        birthday_animal DATE, commands_animal TEXT, genus_id INTEGER)'''
        self.execute(sql, commit=True)

    def create_table_hamsters(self):
        sql = '''CREATE TABLE IF NOT EXISTS hamsters 
        (id_animal INTEGER PRIMARY KEY AUTOINCREMENT, name_animal TEXT,
        birthday_animal DATE, commands_animal TEXT, genus_id INTEGER)'''
        self.execute(sql, commit=True)

    def add_animal(self, name_table: str, new_data: dict):
        parameters = (new_data.get('name'), new_data.get('birthday'),
                      new_data.get('genus_id'))
        sql = f'''INSERT INTO {name_table} (name_animal, birthday_animal, genus_id) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_all_animal(self, name_table: str):
        sql = f'''SELECT * FROM {name_table}'''
        return self.execute(sql, fetchall=True)

    def get_animal(self, name_table: str, **kwargs):
        sql = f'''SELECT * FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def update_animal(self, name_table: str, name_col: str, new_data: dict):
        parameters = (new_data.get('value'), new_data.get('id'))
        sql = f'''UPDATE {name_table} SET {name_col}=? WHERE id_animal=? '''
        self.execute(sql, parameters, commit=True)

    def remove_animal(self, name_table: str, **kwargs):
        sql = f'''DELETE FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)
