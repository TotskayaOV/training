import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def root():
    logger.info("Отработал GET запрос.")
    return {"message": "Hello world!"}


@app.get("/item/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f"Отработал PUT запрос для item id {item_id}.")
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Отработал DELETE запрос для item id {item_id}.")
    return {"item_id": item_id}
