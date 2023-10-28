import pytest
from Unit_tests.NumbersList import NumberList

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
