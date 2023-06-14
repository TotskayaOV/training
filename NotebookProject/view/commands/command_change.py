from .command import Command


class CommandChange(Command):

    def __init__(self, console):
        self.console = console


    @property
    def description(self):
        return "Изменить заметку"


    def execute(self):
        self.console.change_note()
