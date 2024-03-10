from pydantic import BaseModel

class Task(BaseModel):
    task: str
    description: str = None
    status: str
    creationAt: str = None
    updatedAt: str = None
    finishedAt: str = None
    user_id: int = None