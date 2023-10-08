from .command import Command


class CommandShowAll(Command):

    def __init__(self, console):
        self.console = console


    @property
    def description(self):
        return "Показать все заметки"


    def execute(self):
        self.console.show_all()