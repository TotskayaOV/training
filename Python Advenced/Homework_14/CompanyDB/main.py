from company import Company


if __name__ == '__main__':
    nike = Company('NIKE')
    # print(*nike.employees, sep='\n')
    me = nike.login('Феврония Геннадиевна Самойлова', '819334')
    nike.hiring(me, 'Кривой Сергей', 3, '627823')