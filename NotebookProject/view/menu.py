from loguru import logger
from .commands import *


class Menu:


    @logger.catch
    def __init__(self, console):
        self.commands = []
        self.commands.append(CommandShowAll(console))
        self.commands.append(CommandAdd(console))
        self.commands.append(CommandChange(console))
        self.commands.append(CommandRemove(console))
        self.commands.append(CommandExit(console))


    @logger.catch
    def __str__(self):
        """
        :return: str возвращает строковое представление меню
        """
        menu_string = "\nГлавное меню:"
        for index, element in enumerate(self.commands, start=1):
            menu_string += f"\n\t{index}. {element.description}"
        return menu_string

    @logger.catch
    def get_size_menu(self):
        """
        :return: int возвращает длинну списка
        """
        return len(self.commands)

    @logger.catch
    def execute(self, index):
        option = self.commands[index]
        option.execute()
