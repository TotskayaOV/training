import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

task_list = []


@app.get("/")
async def root():
    return {"message": "Hello world"}

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


@app.get("/task/{task_id}")
async def read_task(task_id: int, q: str = None):
    if task_id == 0:
        return task_list
    else:
        for task in task_list:
            if task.get("id") == task_id:
                return {"task_id": task.get("id"), "q": task.get("title")}


@app.post("/task/")
async def create_item(task: Task):
    task_list.append(task)
    logger.info('Отработал POST запрос.')
    return task

@app.put("/task/{task_id}")
async def update_item(task_id: int, task: Task):
    for task in task_list:
        if task.get("id") == task_id:
            task["status"] = "update"
            logger.info(f"Отработал PUT запрос для item id {task_id}.")
            return {"task_id": task_id, "item": task}
    logger.info(f"Отработал PUT запрос для item id {task_id}. Task не найден")
    return {"task_id": task_id, "item": "not found"}


@app.delete("/task/{task_id}")
async def delete_item(task_id: int):
    for i in range(len(task_list)):
        if task_list[i].get("id") == task_id:
            task_list.pop(i)
            logger.info(f"Отработал DELETE запрос для item id {task_id}.")
            return {"task_id": task_id}
    logger.info(f"Отработал DELETE запрос для item id {task_id}.")
    return {"task_id": task_id, "item": "not found"}



for i in range(10):
    id = i+1
    title = f"Title{i+1}"
    description = f"Description{i+1}"
    status = "status"
    task_list.append({'id': id,
                      'title': title,
                      'description': description,
                      'status': status})
