from .command import Command


class CommandExit(Command):

    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        return "Завершить работу"

    def execute(self):
        self.console.finish()
