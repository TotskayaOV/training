import logging
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

task_list = []


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/task/")
async def read_tasks():
    logger.info(f'Отработал GET запрос. All tasks')
    return task_list


@app.get("/task/{task_id}")
async def read_task(task_id: int, q: str = None):
    for task1 in task_list:
        if task1.id == task_id:
            logger.info(f'Отработал GET запрос. Task {task_id}')
            return {"task_id": task1.id, "q": task1.title}
    return {"message": "not found"}


@app.post("/task/")
async def create_task(task: Task):
    task_list.append(task)
    logger.info('Отработал POST запрос.')
    return task


@app.put("/task/{task_id}")
async def update_task(task_id: int, task: Task):
    for task1 in task_list:
        if task1.id == task_id:
            task1 = task
            logger.info(f"Отработал PUT запрос для item id {task_id}.")
            return {"task_id": task_id, "item": task}
    logger.info(f"Отработал PUT запрос для item id {task_id}. Task не найден")
    return {"message": "not found"}


@app.delete("/task/{task_id}")
async def delete_task(task_id: int):
    for i in range(len(task_list)):
        if task_list[i].id == task_id:
            task_list.pop(i)
            logger.info(f"Отработал DELETE запрос для item id {task_id}.")
            return {"task_id": task_id}
    logger.info(f"Отработал DELETE запрос для item id {task_id}.")
    return {"task_id": task_id, "item": "not found"}


for i in range(10):
    task = Task(id=i+1,
                title=f"Title{i+1}",
                description=f"Description{i+1}",
                status="active")
    task_list.append(task)
