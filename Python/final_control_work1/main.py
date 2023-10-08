class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        print("Список команд:", self.commands)

    def train(self, new_commands):
        self.commands.extend(new_commands)


class DomesticAnimal(Animal):
    pass


class WorkingAnimal(Animal):
    pass


class Dog(DomesticAnimal):
    pass


class Horse(WorkingAnimal):
    pass

class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None or self.value > 0:
            raise Exception("Ошибка работы с объектом Счетчик или ресурс остался открыт")
        else:
            print("Ресурс успешно закрыт")


def main():
    animals = []
    counter = Counter()

    animal_classes = {
        "Domestic": Animal,
        "Working": Animal,
        "Dog": Animal,
        "Horse": Animal
    }

    while True:
        print("Меню:")
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд животного")
        print("4. Обучить животное новым командам")
        print("5. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            try:
                with counter:
                    name = input("Введите имя животного: ")
                    animal_type = input("Введите тип животного: ")
                    if animal_type in animal_classes:
                        animal_class = animal_classes[animal_type]
                        animal = animal_class(name, animal_type)
                        animals.append(animal)
                        counter.add()
                    else:
                        print("Некорректный тип животного")
            except Exception as e:
                print(e)

        elif choice == "2":
            name = input("Введите имя животного: ")
            animal_type = input("Введите тип животного: ")
            found = False
            for animal in animals:
                if animal.name == name and animal.animal_type == animal_type:
                    print("Животное принадлежит к классу", animal.animal_type)
                    found = True
                    break
            if not found:
                print("Животное не найдено")

        elif choice == "3":
            name = input("Введите имя животного: ")
            animal_type = input("Введите тип животного: ")
            found = False
            for animal in animals:
                if animal.name == name and animal.animal_type == animal_type:
                    animal.show_commands()
                    found = True
                    break
            if not found:
                print("Животное не найдено")

        elif choice == "4":
            name = input("Введите имя животного: ")
            animal_type = input("Введите тип животного: ")
            found = False
            for animal in animals:
                if animal.name == name and animal.animal_type == animal_type:
                    new_commands = input("Введите новые команды через запятую: ").split(",")
                    animal.train(new_commands)
                    found = True
                    break
            if not found:
                print("Животное не найдено")

        elif choice == "5":
            break

        else:
            print("Некорректный выбор")


if __name__ == "__main__":
    main()
