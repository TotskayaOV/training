from loguru import logger

from modul import LoaderDataBase
from view import Console
from presenter import Presenter


if __name__ == '__main__':
    logger.add("./debug.log", format='{time} {level} {message}', rotation='1 week', compression='zip')
    model = LoaderDataBase()
    view = Console()
    presenter = Presenter(view, model)
    view.start()

