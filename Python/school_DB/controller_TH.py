import view_TH
import modul
import controller

teacher_data = []

def choise_subjekt():
    global teacher_data
    for key, value in modul.techer_dict.items():
        if teacher_data[0] and teacher_data[1] in value:
            id_class = key
    student_list = []
    for k, v in modul.summary_dict.items():
        if id_class == v[0]:
            student_list.append(k)
    view_TH.show_students(modul.people_dict, student_list)      
    temp_dict = modul.reiting_dict[student_list[0]]
    temp_k_list = list(temp_dict.keys())
    str_subj = temp_k_list[view_TH.show_subject(temp_k_list) - 1]
    start_lesson(student_list, str_subj)
    
def start_lesson(st_list: list, num_subj: str):
    x = False
    while x == False:
        id_student = st_list[view_TH.choose_victim() - 1]
        new_raiting = view_TH.change_raiting()
        for keys, value in modul.reiting_dict.items():
            if keys == id_student:
                (value.get(num_subj)).append(new_raiting)
                th_choise = view_TH.close_lesson()
                if th_choise == 2:
                            teacher_menu()

def teacher_menu():
    inp = view_TH.start_stop()
    match inp:
        case 1: choise_subjekt()
        case 2: controller.input_handler(51)


def start():
    global teacher_data
    teacher_data = view_TH.person_chois()
    teacher_menu()

