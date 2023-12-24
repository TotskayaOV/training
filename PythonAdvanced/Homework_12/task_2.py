# 📌Создайте класс-генератор.
# 📌Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# 📌Если переданы два параметра, считаем step=1.
# 📌Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, start: int, stop: int = None, step: int = None):
        self.stop = stop if stop else start
        self.start = start if stop else 1
        self.step = step if step else 1
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            self.result = self.result * (self.start + self.step)
            self.start = self.start + self.step
            return self.result
        raise StopIteration


if __name__ == '__main__':
    a = Factorial(10)
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())