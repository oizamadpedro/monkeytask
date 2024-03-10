from fastapi import APIRouter
from fastapi.responses import Response
from task.services.taskService import TaskService
from task.models.taskModel import Task
import json

router = APIRouter()

@router.get("/task/v1/tasks")
def allTasks():
    tasks = TaskService.getAll()
    return Response(content=json.dumps(tasks),  media_type="application/json", status_code=200)

@router.post("/task/v1/tasks")
def createTask(task: Task):
    idTask = TaskService.create(task)
    return Response(content=json.dumps({"data": idTask}),  media_type="application/json", status_code=201)