import json

class JsonNoteFile:
    def __init__(self, json_path: str = 'modul/notebook_db.json'):
        self.js_path = json_path


    @property
    def connection(self):
        with open(self.js_path, 'w') as file:
            try:
                data = json.load(file)
            except:
                data = None
            else:
                return data
            finally:
                return data



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
        with open(self.js_path, 'w') as file:
            json.dump(file)


    def show_all_notes(self):
        sql = """SELECT * FROM notebook"""
        return self.execute(sql, fetchall=True)


    def add_note_from_db(self, notes: dict):
        data = self.connection()
        if not data:
            data = {1: notes}
            self.disconnect(data)
        else:
            new_index = data.keys()[:-1] + 1
            data[new_index] = notes
            self.disconnect(data)



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



    def disconnect(self, data: dict):
        with open(self.js_path, 'w') as file:
            json.dump(data, file, indent=3)