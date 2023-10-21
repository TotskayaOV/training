import random
import json
from faker import Faker


def create_employee(company: str, count: int):
    employees = {}
    list_id = []
    for _ in range(count):
        name = Faker('ru_rU').name()
        while True:
            employee_id = str(random.randint(1, 999999)).zfill(6)
            if employee_id not in list_id:
                list_id.append(employee_id)
                break
        lvl_access = int(employee_id) % 7 + 1
        if lvl_access in employees:
            employees[lvl_access][employee_id] = name
        else:
            employees[lvl_access] = {employee_id: name}
    with open(f'{company}.json', 'w', encoding='UTF-8') as file:
        json.dump(employees, file, indent=4, ensure_ascii=False)
    return employees
