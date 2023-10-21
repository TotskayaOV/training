from copy import deepcopy


class MyZip:

    __class_lst = None

    # def __new__(cls, value: int, text: str):
    #     instance = super().__new__(cls)
    #     # cls.zip_lst.append(instance)
    #     return instance

    def __init__(self, value: int, text: str):
        self.value = value
        self.text = text
        self.zip_lst = deepcopy(self.__class__.__class_lst)
        if self.__class__.__class_lst is None:
            self.__class__.__class_lst = [self]
        else:
            self.__class__.__class_lst.append(self)

    def __repr__(self):
        return f'MyZip: {self.value}, {self.text}, {self.zip_lst}'


a = MyZip(1, 'пустой список')
b = MyZip(2, 'уже не пустой список')
c = MyZip(3, 'а это никто не увидит')
print(c)
print(a)
print(b)
