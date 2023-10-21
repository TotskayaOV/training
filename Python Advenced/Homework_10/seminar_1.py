# 📌Создайте класс окружность.
# 📌Класс должен принимать радиус окружности при создании экземпляра.
# 📌У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi

class Circle:

    def __init__(self, rad):
        self.rad = rad

    def length_c(self):
        return 2 * self.rad * pi


    def area(self):
        return (self.rad * self.rad) * pi


if __name__ == '__main__':
    circ_1 = Circle(4)
    print(circ_1.length_c())
    print(circ_1.area())