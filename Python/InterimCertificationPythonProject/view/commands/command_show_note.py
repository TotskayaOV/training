from .command import Command


class CommandShowNote(Command):

    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Показать заметку"

    def execute(self):
        self.console.show_note()
