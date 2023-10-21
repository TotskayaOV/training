from .emloyee import Employee


class OwnBasicExeption(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class LevelError(OwnBasicExeption):

    def __init__(self, me, new):
        super(LevelError, self).__init__(f'Ошибка досупа! Служащий ({me.name}, доступ {me.lvl_access}) '
                                         f'не имеет права создавать служащего ({new.name}, доступ {new.lvl_access}) '
                                         f'выше собственного уровня доступа')

class AccessError(OwnBasicExeption):

    def __init__(self, me: Employee):
        super(AccessError, self).__init__(f'Ошибка доступа: Служащий {me.name} ({me.employee_id}) не найден в базе')


class IDValueError(OwnBasicExeption):

    def __init__(self, new_id):
        super(IDValueError, self).__init__(f'ID {new_id} уже существует')
