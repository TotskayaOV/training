# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса


from .pazzl import riddles_game
from .guess import guess_number


__all__ = ['riddles_game', 'guess_number']
