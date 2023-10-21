class UserNumber:

    def __init__(self, number):
        self.number = number
        self.__lower_bound = 25
        self.__upper_bound = 100 + 1


    @property
    def parity(self):
        """
        возвращает True, если число четное и False, если нет
        Метод создаетт свойство объекта "четность", так как данное свойство неизменяемо и зависит от переданного
        числа
        """
        return self.number % 2 == 0

    def belonging_to_interval(self):
        """
        возвращает boolean проверки принадлежности интервалу
        """
        return self.number in range(self.__lower_bound, self.__upper_bound)
