from Calculator.exception_file import DiscountError, NegativePriceError, NegativeDiscountError


class Calculator:

    def add(self, number1: int | float, number2: int | float) -> int | float:
        '''
        метод сложения
        '''
        return number1 + number2

    def subtract(self, number1: int | float, number2: int | float) -> int | float:
        '''
        метод вычитания
        '''
        return number1 - number2

    def multiply(self, number1: int | float, number2: int | float) -> int | float:
        '''
        метод умножения
        '''
        return number1 * number2

    def divide(self, number1: int | float, number2: int | float) -> float:
        '''
        метод деления
        '''
        if number2 != 0:
            return number1 / number2
        else:
            raise ArithmeticError

    def calculate_discount(self, summ_costs: int | float, percent_discount: int | float) -> int | float:
        """
        метод возвращает сумму с учетом скидки
        """
        if isinstance(percent_discount, int | float) and isinstance(summ_costs, int | float):
            if 0 < percent_discount < 100 and summ_costs > 0:
                return self.subtract(summ_costs, self.divide(self.multiply(summ_costs, percent_discount), 100))
            elif percent_discount == 0:
                return summ_costs
            elif percent_discount > 100:
                raise DiscountError(percent_discount)
            elif summ_costs < 0:
                raise NegativePriceError(summ_costs)
            elif percent_discount < 0:
                raise NegativeDiscountError(percent_discount)
        else:
            raise ValueError('Ошибка ввода данных: сумма покупки и процент скидки нужно задать цифрами')
