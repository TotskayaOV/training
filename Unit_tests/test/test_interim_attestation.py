import pytest
from unittest.mock import MagicMock
from Unit_tests.NumbersList import NumberList, UserInput, UserMenu

@pytest.fixture
def list_with_integers():
    return NumberList([1, 2, 3, 4, 5])

@pytest.fixture
def list_with_floats():
    return NumberList([1.5, 2.5, 3.5, 4.5, 5.5])

def test_average_list_with_integers(list_with_integers):
    assert list_with_integers.average_list == 3.0

def test_average_list_with_floats(list_with_floats):
    assert list_with_floats.average_list == 3.5

def test_average_list_empty():
    with pytest.raises(ValueError):
        NumberList([])

def test_compare_lists(list_with_integers, list_with_floats):
    assert list_with_integers.__eq__(list_with_floats) == 'Второй список имеет большее среднее значение'

def test_check_value_with_valid_input():
    nl = NumberList([1, 2, 3, 4, 5])
    assert nl.user_list == [1, 2, 3, 4, 5]

def test_check_value_with_invalid_input():
    with pytest.raises(ValueError):
        NumberList([1, 'abc', 3, 4, 5])

def test_check_value_with_non_list_input():
    with pytest.raises(ValueError):
        NumberList("not a list")


@pytest.fixture
def mocked_user_menu(monkeypatch):
    mocked_menu = MagicMock(spec=UserMenu)
    monkeypatch.setattr(UserMenu, '__init__', mocked_menu.__init__)
    monkeypatch.setattr(UserMenu, '__str__', mocked_menu.__str__)
    return mocked_menu

@pytest.fixture
def user_input():
    return UserInput()

def test_str_menu(mocked_user_menu):
    mocked_user_menu.__str__.return_value = 'Выберите пункт меню:\n1. ввод данных\n2. сравнить списки\n3. выход\n'
    user_menu = UserMenu()
    assert user_menu.__str__() == 'Выберите пункт меню:\n1. ввод данных\n2. сравнить списки\n3. выход\n'

def test_data_update(user_input, monkeypatch):
    user_input._UserInput__first_list = []
    user_input._UserInput__second_list = []

    mocked_new_list = MagicMock(return_value=[1, 2, 3])
    monkeypatch.setattr(user_input, 'new_list', mocked_new_list)

    assert user_input.data_update() == True
    assert user_input._UserInput__first_list == NumberList([1, 2, 3])
    assert user_input._UserInput__second_list == []

def test_equals_list(user_input):
    user_input._UserInput__first_list = NumberList([1, 2, 3])
    user_input._UserInput__second_list = NumberList([1, 2, 3])
    assert user_input.equals_list() == 'Средние значения равны'

    user_input._UserInput__first_list = []
    user_input._UserInput__second_list = []
    assert user_input.equals_list() == 'Для сравнения нужно сначала ввести данные'

    user_input._UserInput__first_list = [1, 2, 3]
    user_input._UserInput__second_list = []
    assert user_input.equals_list() == 'Для сравнения нужно сначала ввести данные'

def test_user_input_false(user_input, monkeypatch):
    user_input._UserInput__first_list = []
    user_input._UserInput__second_list = []

    mocked_new_list = MagicMock(return_value=[1, 'a', 3])
    monkeypatch.setattr(user_input, 'new_list', mocked_new_list)

    assert user_input.data_update() == False
    assert user_input._UserInput__first_list == []
    assert user_input._UserInput__second_list == []

def test_update_data_user_list(user_input):
     assert type(user_input._UserInput__check_number('1')) == int
     assert type(user_input._UserInput__check_number('1.2')) == float
     assert type(user_input._UserInput__check_number('abc')) == str

class TestUserInput:
    @pytest.mark.parametrize('user_input, expected_output', [
        ('1', 'data_input'), # Пример с вводом '1' - ожидаемый результат 'data_input'
        ('2', 'equals_list'),
        ('3', 'exit(0)'),
        ('4', 'Введите номер пункта меню в промежутке от 1 до 3'),
        ('ыаыва', 'Введите номер пункта меню в промежутке от 1 до 3')# Пример с вводом '2' - ожидаемый результат 'equals_list'
        # Добавьте дополнительные сценарии ввода и ожидаемые результаты, если нужно
    ])
    def test_start_menu(self, user_input, expected_output, monkeypatch):
        user_input = UserInput()
        monkeypatch.setattr('builtins.input', MagicMock(return_value=user_input))
        user_input.start_menu()
