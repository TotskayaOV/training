from .command import Command


class CommandAdd(Command):

    def __init__(self, console):
        self.console = console


    @property
    def description(self):
        return "Добавить заметку"


    def execute(self):
        self.console.add_note()
