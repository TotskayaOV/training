from .command import Command


class CommandShowDate(Command):

    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Поиск заметок по дате"

    def execute(self):
        self.console.show_date()
