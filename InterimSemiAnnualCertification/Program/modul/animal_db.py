from .databases import DataBase


class Animals(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_animals(self):
        sql = '''CREATE TABLE IF NOT EXISTS animals 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name_type TEXT)'''
        self.execute(sql, commit=True)

    def add_type(self, new_type: str):
        parameters = (new_type,)
        sql = '''INSERT INTO animals (name_type) VALUES (?)'''
        self.execute(sql, parameters, commit=True)

    def get_type(self, **kwargs):
        sql = f'''SELECT * FROM animals WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def get_all_type(self, **kwargs):
        sql = f'''SELECT * FROM animals'''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def remove_type(self, **kwargs):
        sql = f'''DELETE FROM animals WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)
