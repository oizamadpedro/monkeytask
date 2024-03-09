from fastapi import APIRouter
from fastapi.responses import Response
from services.taskService import TaskService
import json

router = APIRouter()

@router.get("/v1/tasks")
def allTasks():
    tasks = TaskService.getAll()
    return Response(content=json.dumps(tasks),  media_type="application/json", status_code=200)