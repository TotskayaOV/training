class OwnBasicExeption(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class DiscountError(OwnBasicExeption):
    """
    возвращает ошибку если значение скидки превышает 100 %
    """
    def __init__(self, discount):
        super(DiscountError, self).__init__(f'Ошибка размера скидки {discount}: скидка не может быть больше 100 %')


class NegativeDiscountError(OwnBasicExeption):
    """
    возвращает ошибку если значение скидки отрицательная
    """
    def __init__(self, discount):
        super(NegativeDiscountError, self).__init__(f'Ошибка значения скидки {discount}: скидка не может меньше ноля')


class NegativePriceError(OwnBasicExeption):
    """
    возвращает ошибку при попытке ввода отрицательного значения
    """
    def __init__(self, price):
        super(NegativePriceError, self).__init__(f'Ошибка цены {price}: цена не может быть отрицательной')
