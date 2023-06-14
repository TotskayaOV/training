def person_chois():
    last_name = input('Введите фамилию: ').title()
    first_name = input('Введите имя: ').title()
    person_list = []
    person_list.append(last_name)
    person_list.append(first_name)
    return person_list

def show_students(db: dict, student_list: list):
    print()
    for i in range(len(student_list)):
        for key, value in db.items(): 
            if student_list[i] == key:               
                print(f'{i+1}. {value[0]} {value[1]}')
    print()
    
def choose_victim():
    x = False
    print('Кого вызовете к доске?')
    while x == False:
        num_v = input('Введите номер ученика: ')
        try:
            num_v = int(num_v)
            x = True
        except:
            print('Ошибка. Укажите номер ученика цифрой из списка выше.') 
    return num_v
    
def show_subject(subj_list: list):    
    for i in range(len(subj_list)):
        print(f'{i+1}. {subj_list[i]}')
    x = False
    while x == False:
        num_subjekt = input('Введите номер предмета: ')
        try:
            num_subjekt = int(num_subjekt)
            x = True
        except:
            print('Ошибка. Напишите число.')
    return num_subjekt
    
def change_raiting():
    x = False
    while x == False:
        num_reiting = input('Введите оценку: ')
        try:
            num_reiting = int(num_reiting)
            x = True
        except:
            print('Ошибка. Напишите число.')
    return num_reiting    
    
def close_lesson():
    x = False
    while x == False:
        num = input('1. Вызвать еще одного ученика\n2. Закончить предмет\nВведите номер меню: ')
        try:
            num = int(num)
            x = True
        except:
            print('Ошибка. Напишите число.')
    return num  

def start_stop():
    x = False
    while x == False:
        num = input('1. Выбрать предмет\n2. Выход из программы\nВведите номер меню: ')
        try:
            num = int(num)
            x = True
        except:
            print('Ошибка. Напишите число.')
    return num 