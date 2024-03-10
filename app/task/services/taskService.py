from utils import utils as Utils
from task.models.taskModel import Task
from datetime import datetime

class TaskService:
    def getAll():
        query = "select * from tasks;"
        tasks = Utils.selDB(query)
        return tasks
    
    def create(task: Task):
        query = "insert into tasks(task, description, status, creationAt, updatedAt, finishedAt, user_id) values (%s, %s, %s, %s, %s, %s, %s)"
        values = (task.task, task.description, task.status, datetime.now(), task.updatedAt, task.finishedAt, task.user_id)
        idTask = Utils.insDB(query, values)
        return idTask
    
    def userTasks(user_id):
        query = "select * from tasks where user_id=%s"
        values = (user_id, )
        userTasks = Utils.selDB(query, values)
        return userTasks