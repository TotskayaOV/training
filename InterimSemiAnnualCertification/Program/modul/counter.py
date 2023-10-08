class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None or self.value == 0:
            raise Exception("Ошибка работы с объектом Счетчик или ресурс остался открыт")
        else:
            print("Ресурс успешно закрыт")