class Triangle:

    def __init__(self, side_a: int, side_b: int = None, side_c: int = None):
        self.side_a = side_a
        self.side_b = side_b if side_b else side_a
        self.side_c = side_c if side_c else side_a

    @property
    def exists_triangle(self):
        if self.side_a + self.side_b < self.side_c \
                or self.side_c + self.side_b < self.side_a \
                or self.side_a + self.side_c < self.side_b:
            raise ValueError
        else:
            if self.side_a == self.side_b == self.side_c:
                return ' равносторонний'
            elif self.side_c == self.side_b != self.side_a \
                    or self.side_a == self.side_b != self.side_c \
                    or self.side_c == self.side_a != self.side_b:
                return ' равнобедренный'
            else:
                return ''

    def get_info(self):
        return f'Задан{self.exists_triangle} треугольник со сторонами: {self.side_a}, {self.side_b}, {self.side_c}'


if __name__ == '__main__':
    obj_1 = Triangle(2)
    print(obj_1.get_info())
    obj_2 = Triangle(2, 3)
    print(obj_2.get_info())
    obj_3 = Triangle(2, 3, 4)
    print(obj_3.get_info())
    obj_4 = Triangle(1, 6, 2)
    # print(obj_4.get_info())     # ValueError
