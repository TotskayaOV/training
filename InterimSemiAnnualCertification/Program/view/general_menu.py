from Program.loader import counter
from Program.controller import types_to_str, genus_to_str, commands_to_str
from Program.controller import adding_new_animal, add_new_commands, show_animals


def general_menu():

    while True:
        print("Меню:")
        print("1. Завести новое животное")
        print("2. Посмотреть животных в питомнике")
        print("3. Увидеть список команд животного")
        print("4. Обучить животное новым командам")
        print("5. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            try:
                with counter:
                    name = input("Введите имя животного: ")
                    print(types_to_str())
                    animal_type = input("Введите тип животного из списка предложенного: ")
                    print(genus_to_str(animal_type.lower()))
                    animal_genus = input("Введите вид животного из списка предложенного: ")
                    animal_birthday = input("Введите дату рождения животного в формате 1999-12-31: ")
                    print(adding_new_animal({'type': animal_type.lower(), 'name': name,
                                       'birthday': animal_birthday, 'genus': animal_genus.lower()}))
                    counter.add()
            except Exception as e:
                print(e)

        elif choice == "2":
            first_choise = input("Показать всех животных в питомнике(y) или животных определенного типа(n)? ")
            if first_choise.lower() in ['y', 'yes', 'д', 'да']:
                print(show_animals())
            else:
                print(types_to_str())
                animal_type = input("Введите тип животного из списка предложенного: ")
                second_choise = input("Показать всех животных данного типа(y) или животных определенного вида(n)? ")
                if second_choise.lower() in ['y', 'yes', 'д', 'да']:
                    print(show_animals(types=animal_type.lower()))
                else:
                    try:
                        print(genus_to_str(animal_type.lower()))
                    except:
                        print('Ошибка ввода')
                    else:
                        animal_genus = input("Введите вид животного из списка предложенного: ")
                        print(show_animals(types=animal_type.lower(), genus=animal_genus.lower()))


        elif choice == "3":
            try:
                name = input("Введите имя животного: ")
                animal_type = input("Введите тип животного: ")
                print(commands_to_str(name, animal_type.lower()))
            except:
                print('Ошибка ввода')


        elif choice == "4":
            name = input("Введите имя животного: ")
            animal_genus = input("Введите тип животного: ")
            animal_command = input("Введите новую команду животного: ")
            print(add_new_commands(name, animal_genus.lower(), animal_command.lower()))

        elif choice == "5":
            break

        else:
            print("Некорректный выбор")
