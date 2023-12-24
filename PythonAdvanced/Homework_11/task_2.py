from copy import deepcopy

class Archive:
    _instance = None
    __archive_text = []
    __archive_number = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, text="", number=0):
        self.archive_number = deepcopy(self.__class__.__archive_number)
        self.archive_text = deepcopy(self.__class__.__archive_text)
        self.text = text
        self.number = number
        if text:
            self.__class__.__archive_text.append(text)
        if number:
            self.__class__.__archive_number.append(number)

    def __str__(self):
        text_str = f"Text is {self.text} and number is {self.number}. "
        text_str += f"Also {self.archive_text} and {self.archive_number}"
        return text_str

    def __repr__(self):
        return f"Archive(text={self.text}, number={self.number})"


archive1 = Archive("Запись 1", 42)
print(archive1)

archive2 = Archive("Запись 2", 3.14)
print(archive2)
