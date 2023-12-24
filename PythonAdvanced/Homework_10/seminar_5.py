# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


# Вынесите общие свойства и методы классов в класс Животное.
# 📌Остальные классы наследуйте от него.
# 📌Убедитесь, что в созданные ранее классы внесены правки.


class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):

    def __init__(self, name: str, age: int, spec):
        super().__init__(name, age)
        self.spec = spec


class Cat(Animal):

    def __init__(self, name: str, age: int, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):

    def __init__(self, name: str, age: int, spec):
        super().__init__(name, age)
        self.spec = spec

if __name__ == '__main__':
    dog_1 = Dog('Bim', 5, 'лает')
    cat_1 = Cat('Marusia', 3, 'спит')
    bird_1 = Bird('Jeck', 1, 'поет')

    for pet in [dog_1, cat_1, bird_1]:
        print(f'{pet.name} {pet.get_spec()}')
