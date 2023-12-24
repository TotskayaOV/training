UPPER_LVL = 7
LOWER_LVL = 1
LEN_ID = 6


class EmployeeName:

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if not all([all(list(map(lambda x: x.isalpha(), name))) for name in value.split()]):
            raise ValueError(f'Имя может состоять только из букв: {value}')
        if not all(map(lambda x: x.istitle(), value.split())):
            raise ValueError(f'Имена должны быть с большой буквы: {value}')
        setattr(instance, self.parameter_name, value)


class EmployeeID:

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if not len(value) == LEN_ID:
            raise ValueError(f'ID должен быть шестизначным: {value}')
        if not value.isdigit():
            raise ValueError(f'ID должен содержать только цифры: {value}')
        setattr(instance, self.parameter_name, value)


class Employee:
    name = EmployeeName()
    employee_id = EmployeeID()

    def __init__(self, name: str, lvl_access: int, employee_id: str):
        self.name = name
        self.employee_id = employee_id
        if LOWER_LVL <= int(lvl_access) <= UPPER_LVL:
            self.lvl_access = int(lvl_access)
        else:
            raise ValueError(f'Такого уровня доступа не существует: {lvl_access}')

    def __str__(self):
        return f'{self.name} {self.employee_id} | Доступ: {self.lvl_access}'

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.employee_id == other.employee_id
        else:
            return False
