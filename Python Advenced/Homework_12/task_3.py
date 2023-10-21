class Value:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_'+ name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        setattr(instance, self.param_name, self._validate(value))

    def _validate(self, value):
        if not(self.min_value < value < self.max_value):
            raise ValueError
        return value

class Rectangle:
    # __slots__ = ['_width', '_height']
    width = Value(10, 100)
    height = Value(10, 100)
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @property
    def perimeter(self):
        return 2 * (self.width + self._height)

    @property
    def area(self):
        return self.width * self._height

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self._height}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self._height})"

    # @property
    # def width(self):
    #     return self._width
    #
    # @width.setter
    # def width(self, value):
    #     if value <= 0:
    #         raise ValueError('Сторона не может быть отрицательной')
    #     self._width = value
    #
    # @property
    # def height(self):
    #     return self._height
    #
    # @height.setter
    # def height(self, value):
    #     if value <= 0:
    #         raise ValueError('Сторона не может быт отрицательной')
    #     self._height = value


if __name__ == '__main__':
    r1 = Rectangle(11, 21)
    print(r1.area)
    # r1.width = -1