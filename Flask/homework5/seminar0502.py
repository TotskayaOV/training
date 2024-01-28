# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

import logging
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

movies = []


@app.get("/")
async def root():
    return {"message": "Hello movie"}


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


@app.get("/movies/")
async def read_movies():
    logger.info(f'Отработал GET запрос. All movies')
    return movies


@app.get("/task/{genre}")
async def read_genre(genre: str):
    temp_list = []
    for movie in movies:
        if movie.genre == genre:
            temp_list.append(movie)
    if len(temp_list) > 0:
        logger.info(f'Отработал GET запрос. {genre}')
        return {"genre": genre, "list": temp_list}
    else:
        logger.info(f'Отработал GET запрос. {genre} не найден')
        return {"message": "not found"}


name_movie = ['Зеленая миля', 'Криминальное чтиво', 'Форрест Гамп', 'Общество мертвых поэтов', 'Бойцовский клуб',
              'Умница Уилл Хантинг', 'Побег из Шоушенка']
genre_list = ['драма', 'комедия', 'драма', 'комедия', 'триллер', 'мелодрама', 'драма']


for i in range(6):
    movie = Movie(id=i+1,
                title=name_movie[i],
                description=f"Description{i+1}",
                genre=genre_list[i])
    movies.append(movie)

