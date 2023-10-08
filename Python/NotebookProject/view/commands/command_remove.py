from .command import Command


class CommandRemove(Command):

    def __init__(self, console):
        self.console = console


    @property
    def description(self):
        return "Удалить заметку"


    def execute(self):
        self.console.remove_note()
