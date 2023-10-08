import sqlite3


class DataBase:
    def __init__(self, db_path: str = 'modul/notebook_db.db'):
        self.db_path = db_path


    @property
    def connection(self):
        return sqlite3.connect(self.db_path)


    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data


    def create_notebook(self):
        sql = '''CREATE TABLE IF NOT EXISTS notebook 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_created DATETIME, note TEXT)'''
        self.execute(sql, commit=True)

    def show_all_notes(self):
        sql = """SELECT * FROM notebook"""
        return self.execute(sql, fetchall=True)


    def add_note_from_db(self, notes: dict):
        parameters = (notes.get('date_created'), notes.get('note'))
        sql = '''INSERT INTO notebook (date_created, note) 
        VALUES (?, ?)'''
        self.execute(sql, parameters, commit=True)


    def update_notes(self, notes: dict):
        parameters = (notes.get('date_created'), notes.get('note'), notes.get('id'))
        sql = '''UPDATE notebook SET date_created=?, note=? WHERE id=? '''
        self.execute(sql, parameters, commit=True)


    def get_notes(self, **kwargs):
        sql = '''SELECT * FROM notebook WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)


    def remove_notes(self, id: int):
        parameters = (id,)
        sql = '''DELETE FROM notebook WHERE id=?'''
        self.execute(sql, parameters, commit=True)

    @staticmethod
    def extract_kwargs(sql, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())


    def disconnect(self):
        self.connection.close()
