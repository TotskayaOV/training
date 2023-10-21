class Control:

    def __init__(self):
        self.presenter = None

    @staticmethod
    def get_index(size, text):
        """
        Возвращает корректный индекс для списка заметок или меню
        :param size: int задает предельное значение
        :param text: str ввод пользователя
        :return: int индекс
        """
        while True:
            user_input = input(text)
            if (user_input.isdigit() and 1 <= int(user_input) <= size):
                index = int(user_input) - 1
                return index
            else:
                print(f"\nВведите число от 1 до {size}")
