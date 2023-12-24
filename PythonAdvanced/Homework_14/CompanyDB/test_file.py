import pytest
from .emloyee import Employee
from .company import Company
from .script_human import create_employee
from .errors_file import AccessError, IDValueError, LevelError
import os


@pytest.fixture(scope='module')
def employee_create():
    return Employee('Мальвина Ивановна Кац', 4, '123456')


def test_valid_equality_objects(employee_create):
    assert employee_create == Employee('Мальвина Ивановна Кац', 4, '123456')


def test_valid_inequality_objects(employee_create):
    assert not employee_create == Employee('Мальвина Ивановна Кац', 4, '839255')


def test_invalid_employee_name_format():
    with pytest.raises(ValueError):
        Employee('дж0н', 2, '123456')


def test_invalid_employee_name_capitalization():
    with pytest.raises(ValueError):
        Employee('ДЖОН', 2, '123456')


def test_invalid_employee_len_id():
    with pytest.raises(ValueError):
        Employee('Джон', 2, '12345')


@pytest.fixture(scope='module')
def files_create():
    return create_employee('abibas', 20)


def test_file_exists():
    assert os.path.exists('abibas.json')


@pytest.fixture(scope='module')
def company_create():
    return Company('abibas')


@pytest.fixture(scope='module')
def employee_admin(files_create):
    lvl_access = list(files_create.keys())
    lvl_access.sort()
    for k, v in files_create.get(lvl_access[-1]).items():
        object_ = Employee(v, lvl_access[-1], k)
    return object_


@pytest.fixture(scope='module')
def employee_intern(files_create):
    lvl_access = list(files_create.keys())
    lvl_access.sort()
    for k, v in files_create.get(lvl_access[0]).items():
        object_ = Employee(v, lvl_access[0], k)
    return object_


def test_login(files_create, company_create, employee_admin):
    assert company_create.login(employee_admin.name, employee_admin.employee_id)


def test_not_login(company_create, employee_create):
    with pytest.raises(AccessError):
        company_create.login(employee_create.name, employee_create.employee_id)


def test_new_id(company_create, employee_admin, employee_intern):
    with pytest.raises(IDValueError):
        company_create.hiring(employee_admin, 'Иванов Иван Иванович', 1, employee_intern.employee_id)


def test_hiring(company_create, employee_admin, employee_create):
    assert company_create.hiring(employee_admin, employee_create.name, 1, employee_create.employee_id) is None


def test_not_access_hiring(company_create, employee_intern, employee_admin):
    with pytest.raises(LevelError):
        company_create.hiring(employee_intern,
                              employee_admin.name, employee_admin.lvl_access, employee_admin.employee_id)


if __name__ == '__main__':
    pytest.main(['-v'])
