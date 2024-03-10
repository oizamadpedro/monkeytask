from fastapi import APIRouter
from fastapi.responses import Response
from task.services.taskService import TaskService
from task.models.taskModel import Task
from auth.routes import auth as Auth
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import json

security = HTTPBearer()
router = APIRouter()

@router.get("/task/v1/tasks")
def allTasks(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials:
        token = credentials.credentials
        data = Auth.decodeToken(token)
        if "error" in data:
            return data
        else:
            user_id = data['id']  # Assumindo que o ID do usuário está presente no token JWT
            tasks = TaskService.userTasks(user_id)
            return Response(content=json.dumps(tasks), media_type="application/json", status_code=200)
    else:
        return Response(status_code=401, detail="Invalid authorization credentials")

@router.post("/task/v1/tasks")
def createTask(task: Task, credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if token:
        auth = Auth.decodeToken(token)
        user_id = auth.get("id", None)
        if user_id:
            task.user_id = user_id
            idTask = TaskService.create(task)
            return Response(content=json.dumps({"data": idTask}),  media_type="application/json", status_code=201)
    return Response(content=json.dumps({"error": True, "message": "error"}),  media_type="application/json", status_code=500)