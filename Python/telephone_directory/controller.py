import modul
import view

def input_handler(inp: int):
    match inp:
        case 1: view.show_all(modul.db_list)
        case 2: modul.read_db('telephone_directory\database.txt')
        case 3: modul.save_db('telephone_directory\database.txt')
        case 4: modul.set_gb(view.create_newcontact())
        case 5: modul.insert_db(view.change_contact(inp), view.create_contact())
        case 6: modul.delete_db(view.change_contact(inp))
        case 7: modul.save_scv('telephone_directory\database.csv')
        case 8: view.exit_base()


def start():
    while True:
        user_choise = view.user_menu()
        input_handler(user_choise)

  
