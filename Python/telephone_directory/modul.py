import csv
db_list = []
def read_db(path: str)  -> dict:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)
    

def save_db(path: str):
    global db_list
    new_data = []
    for item in db_list:
        contact = ';'.join(item.values())
        contact += '\n'
        new_data.append(contact)
    with open(path, 'w', newline='', encoding='UTF-8') as file:
        for item in new_data:
            file.write(item)


def set_gb(new_data: list):
    global db_list
    db_list.append(new_data)

def insert_db(num_index: int, new_data: dict):
    global db_list
    db_list.pop(num_index - 1)
    db_list.insert(num_index-1, new_data)

def delete_db(num_index: int):
    global db_list
    db_list.pop(num_index - 1)

def save_scv(path: str):
    global db_list
    with open(path, mode="w", encoding='utf-8') as w_file:
        names = ["lastname", "firstname", "phone", "comment"]
        file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                 lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for item in db_list:
            file_writer.writerow({names[0]: item.get(names[0]), names[1]: item.get(names[1]), names[2]: item.get(names[2]), names[3]: item.get(names[3])})