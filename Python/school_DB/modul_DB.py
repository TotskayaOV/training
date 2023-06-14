
def to_dict(data: str):
    journal = {}
    for element in data.split(';'):
        primary_key = element.split(',')[0]        
        value = element.split(',')[1::]
        content_list = []
        for mark in value:
            content_list.append(mark)
        journal.update({primary_key: content_list})        
    return journal

def to_string(dictionary: dict):
    new_string = ''
    for key, value in dictionary.items():
        new_string = new_string + key + ',' +','.join(value)+';'
    return (new_string.rstrip(';'))

def to_reitingdict(data: str):
    journal = {}
    for element in data.split(';'):
        count = 0
        x = True
        while x == True:
            for i in element:
                if i.isdigit():
                    count +=1
                else:
                    x = False
                    break        
        student_key = element[:count]
        student_list = element[count+1::].split('$')
        student_dict = {}
        for student in student_list:
            new = student.split('&!')
            key = new[0]
            value = new[1]
            mark_list = []
            for mark in value.split(','):
                mark_list.append(int(mark))
            student_dict[key] = mark_list
        journal[student_key] = student_dict
    return journal

def to_reitingstring(dictionary: dict):
    new_string = ''
    for key, value in dictionary.items():
        temp_string = ''
        for key2, value2 in value.items():
            temp_string = temp_string + key2 + '&!' +','.join(list(map(str,value2)))+'$'
        new_string = new_string + key + '$' + temp_string.rstrip('$') +';'
    return (new_string.rstrip(';'))
   
def to_adressdict(data: str):
    journal = {}
    for element in data.split(';'):
        primary_key = element.split(',')[0]        
        value = element.split(',')[1::]
        content_list = []
        for mark in value:
            content_list.append(mark)
        journal.update({primary_key: content_list})        
    return journal

def to_adressstring(dictionary: dict):
    new_string = ''
    for key, value in dictionary.items():
        new_string = new_string + key + ',' +','.join(value)+';'
    return (new_string.rstrip(';'))