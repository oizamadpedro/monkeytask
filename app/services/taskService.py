from utils import utils as Utils

class TaskService:
    def getAll():
        query = "select * from tasks;"
        tasks = Utils.selDB(query)
        return tasks