def start_menu() -> int:
    print('Выберите пользователя:')
    menu_list = ['Директор','Учитель', 'Родитель']
    for i in range(len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')
    x = False
    while x == False:
        user_input = input('Введите пункт меню: ')
        try:
            user_input = int(user_input)
            x = True
        except:
            print('Ошибка. Напишите пункт меню.')
    return user_input


def user_menu() -> int:
    print('Меню:')
    menu_list = ['Ученики','Учителя','Класс', 'Оценки', 'Выход']
    menu_people = ['Список учеников', 'Добавить нового ученика', 'Показать адрес ученика', 'Изменить данные ученика']   # 1
    menu_teacher = ['Список учителей', 'Изменить данные учителя', 'Удалить данные об учителе']  # 2
    menu_class = ['Список классов', 'Какие ученики учатся в классе', 'Добавить ученика в класс', 'Удалить ученика из класса'] # 3
    menu_rating = ['Показать оценку ученика', 'Добавить оценку ученику'] # 4
    menu_exit = ['Сохранить и выйти', 'Выйти без сохранения']   # 5
    for i in range(len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')
    x = False
    while x == False:
        user_input = input('Введите пункт меню: ')
        try:
            user_input = int(user_input)
            x = True
        except:
            print('Ошибка. Напишите пункт меню.')
    print(f'Меню "{menu_list[user_input-1]}":')
    user_list = []
    match user_input:
        case 1: user_list = menu_people
        case 2: user_list = menu_teacher
        case 3: user_list = menu_class
        case 4: user_list = menu_rating
        case 5: user_list = menu_exit
    for i in range(len(user_list)):
        print(f'{i+1}. {user_list[i]}')
    x = False
    while x == False:
        user_input2 = input('Введите пункт меню: ')
        try:
            user_input2 = int(user_input2)
            x = True
        except:
            print('Ошибка. Напишите пункт меню.')
    # print(f'(Меню: {user_list}:')
    result_input = user_input * 10 + user_input2
    user_list = []   
    return result_input

#показать список классов
def show_all(db: dict, teacher: dict):
    for key, value in db.items():
        temp_list = teacher[value[1]]
        print(f'{key} . Номер класса: {value[0]} Преподаватель: {temp_list[0]} {temp_list[1]} Кабинет: {value[2]}')
        print()

# показать список учеников/учителей
def show_people(db: dict):    
        for key, value in db.items():                
            print(f'{key} . Фамилия, имя: {value[0]} {value[1]}; дата рождения: {value[2]}')
            print()        

#завершение программы
def exit_base(num: int):   
    if num == 0: 
        print('Завершение программы')
        exit()


# добавить нового ученика/учителя
def create_newcontact_human(our_dict: dict, num: int, change_num: int, general_dict: dict, adr_dict: dict):
    match num:
        case 4 : person = 'ученика'
        case 5 : person = 'учителя'
    if change_num == 0:
        new_key = int(list(our_dict)[::-1][0]) + 1
    else:
        new_key = change_num
    new_content = []
    new_content.append(input(f'Введите Фамилию {person}: '))
    new_content.append(input(f'Введите Имя {person}: '))
    new_content.append(input(f'Введите дату рождения {person}: '))
    our_dict[str(new_key)] = new_content
    if num == 5:
        return our_dict
    else:
        temp_list = []
        temp_list2 =(create_newadress(adr_dict, general_dict, new_key))
        temp_list.append(our_dict)
        temp_list.append(temp_list2[1])
        temp_list.append(temp_list2[0])
        return temp_list


#добавить адрес
def create_newadress(our_dict: dict, general_dict: dict, change_num: int):
    print('Введите адрес ученика.')
    new_content = []
    new_content.append(input(f'Введите город: '))
    new_content.append(input(f'Введите улицу: '))
    new_content.append(input(f'Введите номер дома: '))
    new_content.append(input(f'Введите номер квартиры: '))
    for key, value in our_dict.items():
        if value == new_content:
            num_adres = key
        else:
            num_adres = int(list(our_dict)[::-1][0]) + 1
    our_dict[str(num_adres)] = new_content
    if general_dict.get(str(change_num), 0) == 0:
        general_dict[str(change_num)] = ['', str(num_adres)]
    else:
        general_dict[str(change_num)][1] = str(num_adres)
    temp_list = []
    temp_list.append(our_dict)
    temp_list.append(general_dict)
    return (temp_list)
    

# изменить данные человека 
def choise_transform_contact(n_whoo: int, st_d: dict, tc_d: dict):
    dump_variable = False
    match n_whoo:
            case 1: s_whoo = 'учеников'
            case 2: s_whoo = 'учетелей'    
    while dump_variable == False:
        num_contact = input(f'Введите порядковый номер контакта, который хотите изменить или напишите "список", чтобы показать список {s_whoo}: ')
        if num_contact  == 'список':
            match n_whoo:
                case 1: show_people(st_d)
                case 2: show_people(tc_d)
        else:
            try:
                num_contact = int(num_contact)
                dump_variable = True
            except:
                print('Ошибка. Напишите номер из списка.')        
            return num_contact

# показать кто учится в классе
def run_class(general_dictionary: dict, students_dictionary: dict, cl_dict: dict):
    x = False
    while x == False:
        id_class = input('Введите номер класса: ')
        try:
            id_class = int(id_class)
            x = True
        except:
            print('Ошибка. Напишите пункт меню.')
    print(f'В {cl_dict[str(id_class)][0]} учатся:')
    for key, values in general_dictionary.items():
        if values[0] == str(id_class):
            for id_student, values_student in students_dictionary.items():
                if key == id_student:
                    print(f'{values_student[0]} {values_student[1]}')

# добавить в класс/удалить из класса
def up_dow_class(sum_dict: dict, num_move: int, cl_dict: dict, teacher_dict: dict, stud_dict: dict):
    dump_variable = False       
    while dump_variable == False:
        num_class = input(f'Введите порядковый номер класса или напишите "список", чтобы увидеть список классов: ')
        if num_class  == 'список':
            show_all(cl_dict, teacher_dict)            
        else:
            try:
                num_class = int(num_class)
                dump_variable = True
            except:
                print('Ошибка. Напишите номер из списка.')
    dump_variable = False
    while dump_variable == False:
        num_contact = input(f'Введите порядковый ученика или напишите "список", чтобы увидеть список учеников: ')
        if num_contact  == 'список':
            show_people(stud_dict)            
        else:
            try:
                num_contact = int(num_contact)
                dump_variable = True
            except:
                print('Ошибка. Напишите номер из списка.')
    match num_move:
            case 1: new_value = ''
            case 2: new_value = str(num_class)
    sum_dict[str(num_contact)][0] = new_value    
    return sum_dict           

#показать оценку   
def show_reiting(rt_dict:dict, st_dict: dict):
    x = False
    while x == False:
        id_student = input('Введите номер ученика: ')
        try:
            id_student = int(id_student)
            x = True
        except:
            print('Ошибка. Напишите пункт меню.')
    print(f'{st_dict[str(id_student)][0]} {st_dict[str(id_student)][1]}, оценки:')
    if rt_dict.get(str(id_student), 0) == 0:
        print(f'У ученика {st_dict[str(id_student)][0]} {st_dict[str(id_student)][1]} пока что нет оценок')
    else:
        temp_dict = rt_dict[str(id_student)]
        for key, values in temp_dict.items():
            print(f"{key}: {', '.join(list(map(str, values)))}")

# добавить оценку
def add_reiting(rt_dict:dict, st_dict: dict):
    x = False
    while x == False:
        id_student = input('Введите номер ученика: ')
        try:
            id_student = int(id_student)
            x = True
        except:
            print('Ошибка. Напишите число.')
    if rt_dict.get(str(id_student), 0) == 0:
        temp_dict = rt_dict['1']
        temp_k_list = list(temp_dict.keys())
        temp2_dict = {}
        for k in range(len(temp_k_list)):
            temp2_dict[temp_k_list[k]] = []
        rt_dict[str(id_student)] = temp2_dict     
    temp_dict = rt_dict[str(id_student)]
    temp_k_list = list(temp_dict.keys())
    print('Выберите предмет: ')
    for i in range(len(temp_k_list)):
        print(f'{i+1}. {temp_k_list[i]}')
    x = False
    while x == False:
        num_subjekt = input('Введите номер предмета: ')
        try:
            num_subjekt = int(num_subjekt)
            x = True
        except:
            print('Ошибка. Напишите число.')
    x = False
    while x == False:
        num_reiting = input('Введите оценку: ')
        try:
            num_reiting = int(num_reiting)
            x = True
        except:
            print('Ошибка. Напишите число.')  
    temp_dict[temp_k_list[num_subjekt-1]].append(num_reiting)
    rt_dict[str(id_student)] = temp_dict
    print(f'{st_dict[str(id_student)][0]} {st_dict[str(id_student)][1]} добавили оценку {num_reiting}')
    return rt_dict

# показать адрес
def show_p_adress(general_dictionary: dict, st_dictionary: dict, ad_dict: dict):
    x = False
    while x == False:
        id_people = input('Введите номер ученика: ')
        try:
            id_people = int(id_people)
            x = True
        except:
            print('Ошибка. Напишите пункт меню.')
    print(f'{st_dictionary[str(id_people)][0]} {st_dictionary[str(id_people)][1]} проживает по адресу:')
    id_adress = list(general_dictionary.get(str(id_people)))[1]
    temp_list = list(ad_dict.get(id_adress))
    print(f'{temp_list[0]}, {temp_list[1]}, дом {temp_list[2]}, квартира {temp_list[3]}.')

def is_in_development():
    print('Данная опция временно не доступна.')