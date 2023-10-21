# Задача о равенстве весов: У вас есть 8 монет, одна из которых фальшивая (легче остальных).
# Вам доступны весы без гирь. Каким наименьшим количеством взвешиваний можно определить фальшивую монету и узнать,
# она легче или тяжелее остальных?
from functools import total_ordering


@total_ordering
class Coin:
    def __init__(self, weight):
        self.weight = weight

    def __eq__(self, other):
        if isinstance(other, Coin):
            return self.weight == other.weight
        elif isinstance(other, float | int):
            return self.weight == other
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, Coin):
            return self.weight < other.weight
        elif isinstance(other, float | int):
            return self.weight < other
        else:
            raise TypeError

    def get_param(self):
        return  self.weight

    def __str__(self):
        return f'coin weight {self.weight}'


class CoinColumn:

    _left_column = []
    _right_column = []

    def __init__(self, unit_list: list):
        if len(unit_list) > 1:
            temp_unit = unit_list[0]
            self._left_column = []
            self._right_column = []
            for i in range(1, len(unit_list)):
                if unit_list[i] == temp_unit:
                    self._right_column.append(unit_list[i])
                else:
                    self._left_column.append(unit_list[i])
        else:
            raise ValueError('Количество монет для сравнения должно быть больше 1')

    def find_noncondition(self):
        if len(self._right_column) < len(self._left_column):
            if len(self._right_column) == 1:
                return self._right_column[0]
            return self._right_column
        elif len(self._left_column) < len(self._right_column):
            if len(self._left_column) == 1:
                return self._left_column[0]
            return self._left_column


coins = [
            Coin(10), Coin(10), Coin(10),
            Coin(10), Coin(10), Coin(10),
            Coin(10), Coin(11), Coin(10)
        ]

c_col = CoinColumn(coins)
print(c_col.find_noncondition())
