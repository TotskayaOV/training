def divide_numbers():
    go_program = True
    while go_program:
        try:
            user_input = input("Введите числа для деления через пробел: ")
            a, b = user_input.split(" ")
            if '.' in a: a = float(a)
            else: a = int(a)
            if '.' in b: b = float(b)
            else: b = int(b)
            result = a / b
        except ArithmeticError as err:
            print('Деление на ноль недопустимо')
        except ValueError as err:
            print("Для операции деления нужно 2 числа")
        except Exception as err:
            print(f'Ошибка: {err}')
        else:
            print(f"Ответ: {result}")
        finally:
            check_stop = input("Если хотите попробовать ввести еще раз, нажмите Enter.\n"
                               "Для выхода в главное меню введите любое число или букву: ")
            if check_stop:
                go_program = False

                
def age_check():
    go_program = True
    while go_program:
        try:
            user_input = input("Введите свой возраст: ")
            if '.' in user_input: user_input = float(user_input)
            else: user_input = int(user_input)
        except ValueError:
            print("Некорректный ввод")
        else:
            print(f"Ваш возраст {user_input}")
        finally:
            check_stop = input(
                "Если хотите попробовать ввести еще раз, нажмите Enter.\n"
                "Для выхода в главное меню введите любое число или букву: ")
            if check_stop:
                go_program = False


def read_file():
    try:
        with open('./numbers.csv', 'r', encoding='UTF-8') as file:
                my_list = file.readlines()
                result = 0
                for line in range(0, len(my_list)):
                    temp_string = my_list[line].rstrip("\n")
                    if '.' in temp_string: temp_stringt = float(temp_string)
                    else: temp_string = int(temp_string)
                    result += temp_string
    except ValueError:
        print("Некорректное значение числа в файле")
    else:
        print(f"Сумма цифр в файле: {result}")


def main_menu():
    user_choise = input("Введите номер пунтка меню: ")
    match user_choise:
        case '1': return 1
        case '2': return 2
        case '3': return 3
        case '4': return 4
        case _: return 0


if __name__ == '__main__':
    start_file = True
    while start_file:
        print("Главное меню:\n1. Разделить\n2. Ввести возраст\n3. Сложить цифры в файле\n4. Выход")
        check_choise = main_menu()
        match check_choise:
            case 1: divide_numbers()
            case 2: age_check()
            case 3: read_file()
            case 4:
                print("Хорошего дня!")
                start_file = False
            case 0: print("Ошибка ввода. Введите только цифру.")

