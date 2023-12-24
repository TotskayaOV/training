import os
import json
import csv


class User:
    """
    создание пользователя
    """

    def __init__(self, name: str, id_user: str, lvl: str):
        self.name = name
        self.id_user = id_user
        self.lvl = lvl

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id_user

    def get_lvl(self):
        return self.lvl

class JsonDb:
    """
    работа с файлом .json
    """

    def __init__(self, path_db: str):
        self.path_db = path_db
        self.__id_in_db = self.__read_file_id()
        self.__db_dict = self.reading_file()

    def __check_file(self):
        """
        проверяет есть ли файл
        """
        if os.path.exists(self.path_db):
            with open(self.path_db, 'r', encoding='UTF-8') as f:
                return json.load(f)
        else:
            return {}

    def __read_file_id(self):
        """
        формирует список с id
        """
        json_dict = self.__check_file()
        if json_dict:
            return [int(key) for elem in list(json_dict.values()) for key, values in elem.items()]
        else:
            return []

    def reading_file(self):
        """
        читает json файл
        """
        json_dict = self.__check_file()
        return json_dict if json_dict else {}

    def check_id(self, id_num):
        """
        проверяет занят ли id
        """
        if int(id_num) in self.__id_in_db:
            return False
        else:
            return True

    def write_file(self, new_obj: User):
        """
        запись в файл
        """
        lvl_dict = self.__db_dict.get(str(new_obj.get_lvl()), {})
        lvl_dict[new_obj.get_id()] = new_obj.get_name()
        self.__db_dict[str(new_obj.get_lvl())] = lvl_dict
        with open(self.path_db, 'w', encoding='UTF-8') as f:
            json.dump(self.__db_dict, f, indent=4, ensure_ascii=False)
        self.__id_in_db.append(int(new_obj.get_id()))


class CsvFile:
    """
    работа с файлом .csv
    """

    def __init__(self, path_file, delimiter, encoding, lineterminator):
        self.path_file = path_file
        self.delimiter = delimiter
        self.encoding = encoding
        self.lineterminator = lineterminator

    def write_csv(self, json_obj: JsonDb):
        """
        конвертация json в csv
        """
        json_data = json_obj.reading_file()
        with open(self.path_file, 'w+', encoding=self.encoding) as file_csv:
            csv_writer = csv.writer(file_csv, delimiter=self.delimiter, lineterminator=self.lineterminator)
            csv_writer.writerow(("ID", "Имя", "Уровень доступа"))
            if json_data:
                for lvl, values in json_data.items():
                    for id_u, name in values.items():
                        csv_writer.writerow([id_u, name, lvl])



class UserInput:
    """
    пользовательский ввод
    """

    def __init__(self, path_db):
        self.db = JsonDb(path_db)
        self.__lower = 0
        self.__upper = 8

    def _input_name(self) -> str:
        user_input_name = input('Введите имя или введите exit для выхода из программы: ')
        if user_input_name == 'exit':
            return False
        return user_input_name

    def _input_id_user(self) -> int:
        while True:
            user_input_id = input('Введите id пользователя: ')
            if self.db.check_id(user_input_id) is True:
                return user_input_id
            else:
                print('Такой id уже существует')

    def _input_level_access(self) -> int:
        while True:
            user_input_level = input('Введите уровень доступа: ')
            if user_input_level.isdigit():
                if self.__lower < int(user_input_level) < self.__upper:
                    return user_input_level
                else:
                    continue
            else:
                continue

    def created_new_user(self):
        name = self._input_name()
        if name:
            new_user = User(name, self._input_id_user(), self._input_level_access())
            self.db.write_file(new_user)
            return True
        else:
            return False

    def uploading_to_сsv(self):
        user_input = input('Хотите выгрузить данные в файл csv?(y|n): ')
        if user_input in ('y', 'Y', 'д', 'Д', 'да', 'Да', 'yes', 'Yes'):
            obj_csv = CsvFile('./csv_db.csv', delimiter=',', encoding='UTF-8', lineterminator='\r')
            obj_csv.write_csv(self.db)



if __name__ == '__main__':
    obj_1 = UserInput('./json_db.json')
    infinite_input = True
    while infinite_input:
       infinite_input = obj_1.created_new_user()
    obj_1.uploading_to_сsv()
