import databases
import sqlalchemy
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from faker import Faker


app = FastAPI()

DATABASE_URL = "sqlite:///my_database.db"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128))
)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False})
metadata.create_all(engine)


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     """
#     создание фейковых пользователей
#     """
#     for i in range(count):
#         query = users.insert().values(name=Faker().name(), email=Faker().email())
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


@app.post("/users/", response_model=User)
async def crate_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    # query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), 'id': last_record_id}


@app.get("/users/", response_model=list[User])
async def read_users():
    query =users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id:int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# class Item(BaseModel):
#     name: str = Field(..., title="Name", max_length=50)
#     price: float = Field(..., title="Price", gt=0, le=100000)
#     description: str = Field(default=None, title="Description", max_length=1000)
#     tax: float = Field(0, title="Tax", ge=0, le=10)
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return {"item": item}

