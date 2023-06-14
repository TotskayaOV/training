import view_DB as view
import modul
import controller_TH

def rol_choise(inp: int):
    while True:
        if modul.people_dict:
            match inp:
                case 1:
                    user_choise = view.user_menu()
                    input_handler(user_choise)                
                case 2:
                    controller_TH.start()
                case 3:
                    view.is_in_development()
                    input_handler(52)                   
        else:
            modul.list_dictionaries()
    

def input_handler(inp: int):
    match inp:
        case 11: view.show_people(modul.people_dict)
        case 12:
            temp_list = view.create_newcontact_human(modul.people_dict, 4, 0, modul.summary_dict, modul.adress_dict)
            modul.list_save(temp_list[0], 1)
            modul.list_save(temp_list[1], 4)
            modul.list_save(temp_list[2], 6)
        case 13: view.show_p_adress(modul.summary_dict, modul.people_dict, modul.adress_dict)
        case 14: 
            temp_list = view.create_newcontact_human(modul.people_dict, 4, view.choise_transform_contact(1, modul.people_dict, modul.techer_dict), modul.summary_dict, modul.adress_dict)
            modul.list_save(temp_list[0], 1)
            modul.list_save(temp_list[1], 4)
            modul.list_save(temp_list[2], 6)
        case 21: view.show_people(modul.techer_dict)
        case 22: modul.list_save(view.create_newcontact_human(modul.techer_dict, 5, view.choise_transform_contact(2, modul.people_dict, modul.techer_dict), modul.summary_dict, modul.adress_dict), 2)
        case 31: view.show_all(modul.class_dict, modul.techer_dict)
        case 32: view.run_class(modul.summary_dict, modul.people_dict, modul.class_dict)
        case 33: modul.list_save(view.up_dow_class(modul.summary_dict, 2, modul.class_dict, modul.techer_dict, modul.people_dict), 4)
        case 34: modul.list_save(view.up_dow_class(modul.summary_dict, 2, modul.class_dict, modul.techer_dict, modul.people_dict), 4)
        case 41: view.show_reiting(modul.reiting_dict, modul.people_dict)
        case 42: modul.list_save(view.add_reiting(modul.reiting_dict, modul.people_dict), 5)
        case 51: view.exit_base(modul.overwriting_file())
        case 52: view.exit_base(0)


def start():
    user_choise = view.start_menu()
    rol_choise(user_choise)
