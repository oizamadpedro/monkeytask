from utils import utils as Utils
from task.models.taskModel import Task
from datetime import datetime

class TaskService:
    def getAll():
        query = "select * from tasks;"
        tasks = Utils.selDB(query)
        return tasks
    
    def create(task: Task):
        query = "insert into tasks(task, description, status, creationAt, updatedAt, finishedAt) values (%s, %s, %s, %s, %s, %s)"
        values = (task.task, task.description, task.status, datetime.now(), task.updatedAt, task.finishedAt)
        idTask = Utils.insDB(query, values)
        return idTask