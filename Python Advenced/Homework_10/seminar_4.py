# 📌Создайте класс Сотрудник.
# 📌Воспользуйтесь классом человека из прошлого задания.
# 📌У сотрудника должен быть: ○ шестизначный идентификационный номер ○ уровень доступа вычисляемый как остаток
# от деления суммы цифр id на семь

from seminar_3 import Person


class Worker(Person):

    def __init__(self, id_number: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_number = id_number
        self.lvl = sum(list(map(int, id_number))) % 7


if __name__ == '__main__':
    work_1 = Worker('9873592', 'Smit', 'Ivan', 32)
    print(work_1.full_name())
    print(work_1.id_number)
    print(work_1.lvl)
