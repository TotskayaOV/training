from .user_menu import UserMenu
from .number_list import NumberList


class UserInput:

    def __init__(self):
        self.__first_list = []
        self.__second_list = []

    def start_menu(self):
        user_menu = UserMenu()
        user_input = input(user_menu)
        if user_input == '1':
            self.data_input()
        elif user_input == '2':
            print(self.equals_list())
        elif user_input == '3':
            exit(0)
        else:
            print(f'Введите номер пункта меню в промежутке от 1 до {len(user_menu.menu_list)}')

    def __check_number(self, us_str):
        if '.' in us_str:
            us_list = us_str.split('.')
            if all(item.isdigit() for item in us_list):
                return float(us_str)
            else:
                return us_str
        elif us_str.isdigit():
            return int(us_str)
        else:
            return us_str

    def new_list(self):
        user_list = input('Введите данные нового списка через пробел: ').split()
        return [self.__check_number(elem) for elem in user_list]

    def data_update(self):
        result_list = self.new_list()
        try:
            if not isinstance(self.__first_list, NumberList):
                self.__first_list = NumberList(result_list)
            elif not isinstance(self.__second_list, NumberList):
                self.__second_list = NumberList(result_list)
            else:
                self.__first_list = NumberList(result_list)
                self.__second_list = []
        except ValueError as err:
            print(err)
            return False
        else:
            return True


    def data_input(self):
        cnt = 2
        while cnt != 0:
            check_input = self.data_update()
            if check_input:
                cnt -= 1

    def equals_list(self):
        if isinstance(self.__first_list, NumberList) and isinstance(self.__second_list, NumberList):
            return self.__first_list == self.__second_list
        elif not isinstance(self.__first_list, NumberList) or not isinstance(self.__second_list, NumberList):
            return 'Для сравнения нужно сначала ввести данные'




if __name__ == '__main__':
    obj_1 = UserInput()
    while True:
        obj_1.start_menu()

