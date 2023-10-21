import pytest
from Calculator import Calculator, DiscountError, NegativePriceError, NegativeDiscountError


@pytest.fixture()
def create_calculator():
    """
    создаем объект калькулятор, который будет использоваться во всех тестах
    """
    return Calculator()


def test_addition(create_calculator):
    """
    проверка метода суммирования
    """
    assert create_calculator.add(10, 12.2) == 22.2


def test_division(create_calculator):
    """
    проверка деления
    """
    assert create_calculator.divide(4, 2) == 2


def test_division_error(create_calculator):
    """
    проверка деления на ноль
    """
    with pytest.raises(ArithmeticError):
        create_calculator.divide(2, 0)

def test_discount_1(create_calculator):
    """
    проверка рассчета суммы с учетом скидки 12%
    """
    assert create_calculator.calculate_discount(925, 12) == 814


def test_discount_2(create_calculator):
    """
    проверка рассчета суммы с учетом скидки 30%
    """
    assert create_calculator.calculate_discount(925, 30) == 647.5


def test_discount_3(create_calculator):
    """
    проверка рассчета суммы с учетом скидки 0.4%
    """
    assert create_calculator.calculate_discount(925, 0.4) == 921.3


def test_discount_big(create_calculator):
    """
    проверка рассчета суммы с учетом скидки превышающей 100%
    """
    with pytest.raises(DiscountError):
        create_calculator.calculate_discount(925, 122)


def test_discount_zero(create_calculator):
    """
    проверка рассчета суммы с учетом скидки равной 0%
    """
    assert create_calculator.calculate_discount(925, 0) == 925


def test_negative_discount(create_calculator):
    """
    проверка рассчета суммы с учетом отрицательной скидки
    """
    with pytest.raises(NegativeDiscountError):
        create_calculator.calculate_discount(925, -12)


def test_negative_price(create_calculator):
    """
    проверка расчета суммы с учетом скидки при отрицательной сумме
    """
    with pytest.raises(NegativePriceError):
        create_calculator.calculate_discount(-925, 12)


def test_string_price(create_calculator):
    """
    проверка расчета суммы с учетом скидки при некорректной передаче аргументов (скидка)
    """
    with pytest.raises(ValueError):
        create_calculator.calculate_discount(925, 'two')


def test_string_discount(create_calculator):
    """
    проверка расчета суммы с учетом скидки при некорректной передаче аргументов (сумма)
    """
    with pytest.raises(ValueError):
        create_calculator.calculate_discount('nine hundred and twenty-five', 12)
