import json
import os
from .script_human import create_employee
from .emloyee import Employee
from .errors_file import AccessError, IDValueError, LevelError


class Company:

    def __init__(self, name: str, staff: int = None):
        self.name = name
        self.staff = staff if staff else 10
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json', 'r', encoding='UTF-8') as file:
               employees_list = json.load(file)
        else:
            employees_list = create_employee(self.name, self.staff)
        self.employees = [Employee(e_name, e_lvl, e_id) for e_lvl, person in
                          employees_list.items() for e_id, e_name in person.items()]

    def login(self, name: str, e_id: str):
        for employee in self.employees:
            if employee.name == name and employee.employee_id == e_id:
                return employee
        raise AccessError(Employee(name, 1, e_id))

    def hiring(self, me: Employee, new_name: str, new_lvl: int, new_id: str):
        if me:
            if me.lvl_access > new_lvl:
                if new_id not in [employee.employee_id for employee in self.employees]:
                    self.employees.append(Employee(new_name, int(new_lvl), new_id))
                    self.__save()
                else:
                    raise IDValueError(new_id)
            else:
                raise LevelError(me, Employee(new_name, new_lvl, new_id))
        else:
            raise AccessError(me)

    def __save(self):
        employees_list = {}
        for employee in self.employees:
            if employee.lvl_access in employees_list:
                employees_list[employee.lvl_access][employee.employee_id] = employee.name
            else:
                employees_list[employee.lvl_access] = {employee.employee_id: employee.name}
        with open(f'{self.name}.json', 'w', encoding='UTF-8') as file:
            json.dump(employees_list, file, indent=4, ensure_ascii=False)
