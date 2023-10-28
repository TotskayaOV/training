class UserMenu:

    def __init__(self):
        self.menu_list = ['ввод данных',
                          'сравнить списки',
                          'выход']

    def __str__(self):
        result_str = '\n'.join([f'{elem[0]}. {elem[1]}' for elem in list(enumerate(self.menu_list, 1))])
        return f"Выберите пункт меню:\n{result_str}\n"
