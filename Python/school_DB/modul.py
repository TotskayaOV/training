import modul_DB
people_dict = {}
techer_dict = {}
class_dict = {}
summary_dict = {}
reiting_dict = {}
adress_dict = {}

def dbfile_open(path):
    with open(path, 'r', encoding='UTF-8') as file:
        my_string = file.readline()
        result = modul_DB.to_dict(my_string)
        return result


def dbfile_save(new_dict, path, num_modul):
    if num_modul == 1:
        with open(path, 'w', encoding='UTF-8') as file: 
            file.write(modul_DB.to_string(new_dict))
    else:
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(modul_DB.to_reitingstring(new_dict))

def dbfile_open2(path):
    with open(path, 'r', encoding='UTF-8') as file:
        my_string = file.readline()
        result = modul_DB.to_reitingdict(my_string)
        return result

def list_dictionaries():
    global people_dict
    global techer_dict
    global class_dict
    global summary_dict
    global reiting_dict
    global adress_dict
    people_dict = dbfile_open('school_DB\people_DB.txt')
    techer_dict = dbfile_open('school_DB\cowboys.txt')
    class_dict = dbfile_open('school_DB\class_DB.txt')
    summary_dict = dbfile_open('school_DB\summary_DB.txt')
    reiting_dict = dbfile_open2('school_DB\p_reiting.txt')
    adress_dict = dbfile_open('school_DB\Adress_DB.txt')


def list_save(new_dict: dict, num_dict: int):
    global people_dict
    global techer_dict
    global class_dict
    global summary_dict
    global reiting_dict
    global adress_dict
    match num_dict:
        case 1: people_dict = new_dict
        case 2: techer_dict = new_dict
        case 3: class_dict = new_dict
        case 4: summary_dict = new_dict
        case 5: reiting_dict = new_dict
        case 6: adress_dict = new_dict


def overwriting_file():
    global people_dict
    global techer_dict
    global class_dict
    global summary_dict
    global reiting_dict
    global adress_dict
    dbfile_save(people_dict, 'school_DB\people_DB.txt', 1)
    dbfile_save(techer_dict, 'school_DB\cowboys.txt', 1)
    dbfile_save(class_dict, 'school_DB\class_DB.txt', 1)
    dbfile_save(reiting_dict, 'school_DB\p_reiting.txt', 0)
    dbfile_save(summary_dict, 'school_DB\summary_DB.txt', 1)
    dbfile_save(summary_dict, 'school_DB\Adress_DB.txt', 1)
    return 0
    
