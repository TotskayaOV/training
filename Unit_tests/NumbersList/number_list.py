class NumberList:

    def __init__(self, user_list: list):
        self.user_list = self.__check_value(user_list)

    @property
    def average_list(self) -> float:
        return sum(self.user_list) / len(self.user_list)

    def __check_value(self, user_list):
        if isinstance(user_list, list):
            if len(user_list) == 0:
                raise ValueError('list should not be empty')
            elif all([isinstance(x, int | float) for x in user_list]):
                return user_list
            else:
                raise ValueError('list should contain only numbers')
        else:
            raise ValueError('object accepts only the list type')

    def __eq__(self, other):
        if isinstance(other, NumberList):
            if self.average_list > other.average_list:
                return 'Первый список имеет большее среднее значение'
            elif self.average_list < other.average_list:
                return 'Второй список имеет большее среднее значение'
            else:
                return 'Средние значения равны'
