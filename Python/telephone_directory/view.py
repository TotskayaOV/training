def user_menu() -> int:
    print('Меню:')
    menu_list = ['Показать все контакты',
        'Открыть файл',
        'Сохранить файл',
        'Создать контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Сохранить в формате .csv',
        'Выход']
    for i in range(len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')
    x = False
    while x == False:
        user_input = input('Введи команду: ')
        try:
            user_input = int(user_input)
            x = True
        except:
            print('Ошибка. Напишите пункт меню.')
    return user_input

def show_all(db: list):
    print(db)
    if db_succuss(db):
        for i in range(len(db)):
            user_id = i + 1
            print(user_id, end = '.\t')
            for v in db[i].values():
                print(f'{v}', end = ' ')
            print()

def db_succuss(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False

def exit_base():    
    print('Завершение программы')
    exit()

def create_newcontact():
    print('Создание нового контакта.')
    new_contact = create_contact()
    return new_contact

def create_contact():
    new_contact = dict()
    new_contact['lastname'] = input('Введите фамилию: ')
    new_contact['firstname'] = input('Введите имя: ')
    new_contact['phone'] = input('Введите телефон: ')
    new_contact['comment'] = input('Введите комментарий: ')
    return new_contact

def change_contact(num_move: int):
    if num_move == 5:
        move_str = 'изменить'
    else:
        move_str = 'удалить'
    dump_variable = False
    while dump_variable == False:
        num_contact = input(f'Введите порядковый номер контакта, который хотите {move_str}, или напишите меню, чтобы перейти в главное меню: ')
        try:
            num_contact = int(num_contact)
            dump_variable = True
        except:
            if num_contact == 'меню':
                user_menu()
                dump_variable = True
            else:
                print('Ошибка. Напишите пункт меню.')        
        return num_contact


    
    
