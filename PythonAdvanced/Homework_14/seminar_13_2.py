import json
import os

from seminar_13 import User, load_json
class Loger:
    db = {}
    user_db = {}

    def __init__(self, path):
        self.__class__.db = load_json(path)
        for _id in self.__class__.db:
            self.__class__.user_db[_id] = User(self.__class__.db['name'],
                                               self.__class__.db['_id'],
                                               self.__class__.db['level'])
        self.level = None

    def authorize(self, the_id, name):
        user = User(name, the_id)
        print(user)
        print(self.__class__.db)
        for obj in self.__class__.db.values():
            if user == obj:
                self.level = self.__class__.db[str(the_id)]['level']
                return self.level
            else:
                raise Exception('Пользователь с такими данными не найден')


if __name__ == '__main__':
    PATH = 'my_json.json'
    loger = Loger(PATH)
    print(f"Уровень доступа: {loger.authorize(1, 'Алекс')}")