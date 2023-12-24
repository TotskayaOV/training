# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.


from seminar_5 import Dog, Cat, Bird

class Factory:
    type_list = ['dog', 'cat', 'bird']

    def __init__(self, type_animal, name: str, age: int, spec: str):
        self.type_animal = self.__errors_func(type_animal)
        self.params = (name, age, spec)

    def return_object(self):
        match self.type_animal:
            case 'dog': return Dog(*self.params)
            case 'cat': return Cat(*self.params)
            case 'bird': return Bird(*self.params)

    def __errors_func(self, type_animal):
        if type_animal in self.type_list:
            return type_animal
        else:
            raise ValueError


if __name__ == '__main__':
    obj_1 = Factory('dog', 'Falco', 4, 'voice').return_object()
    print(type(obj_1))
    print(f'{obj_1.name} {obj_1.get_spec()}')
