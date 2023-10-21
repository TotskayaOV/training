from view import Console
from presenter import Presenter


if __name__ == '__main__':
    view = Console()
    presenter = Presenter(view)
    view.start()
