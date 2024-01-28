# Задание №4
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Реализуйте валидацию данных запроса и ответа.

import logging
from faker import Faker
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

users = []


@app.get("/")
async def root():
    return {"message": "Hello Admin"}


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


@app.get("/users/")
async def read_users():
    logger.info(f'Отработал GET запрос. All users')
    return users


@app.post("/new_users/")
async def create_users(user: User):
    for user_old in users:
        if user_old.id == user.id:
            logger.info(f'Попытка добавления {user}. Запрос отклонен')
            return {"message": "Пользователь с таким id уже существует"}
    users.append(user)
    logger.info(f'Отработал POST запрос. Добавлен {user}')
    return user


@app.put("/user/{user_id}")
async def update_user(user_id: int, user: User):
    for user_old in users:
        if user_old.id == user_id:
            user_old = user
            logger.info(f"Отработал PUT запрос для item id {user_id}.")
            return {"task_id": user_id, "item": user}
    logger.info(f"Отработал PUT запрос для item id {user_id}. User не найден")
    return {"message": "not found"}


for i in range(30):
    user = User(id=i+1,
                name=Faker().name(),
                email=Faker().email(),
                password=Faker().password())
    users.append(user)
