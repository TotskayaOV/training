# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Person:

    def  __init__(self, first_name: str, last_name: str, age: int, second_name: str = None):
        self.first_name = first_name
        self.second_name = second_name if second_name else ''
        self.last_name = last_name
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

