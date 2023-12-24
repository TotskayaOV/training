# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌Экземпляр должен запоминать последние k значений.
# 📌Параметр k передаётся при создании экземпляра.
# 📌Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

import json


class Factorial:
    def __init__(self, limit: int):
        self.limit = limit
        self.storage = {}

    def _fact(self, num: int):
        factorial = []
        number = 1
        for i in range(1, num + 1):
            number *= i
            factorial.append(number)
        return factorial

    def __call__(self, number: int):
        result = self._fact(number)[-self.limit:]
        self.storage[number] = result
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        file = open('./fact_dict.json', 'w', encoding='UTF-8')
        json.dump(self.storage, file, indent=4)
        file.close()

if __name__ == '__main__':
    a = Factorial(2)
    print(a(5))
    print(a(10))
    print(a(6))
    print(a.storage)

    with Factorial(4) as fact:
        fact(20)
        fact(5)
        fact(3)
        fact(12)
