from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from task.routes import task
from auth.routes import auth

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://seu-outro-dominio.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique os métodos permitidos
    allow_headers=["*"],  # ou especifique os cabeçalhos permitidos
)

app.include_router(task.router, tags=["tasks"])
app.include_router(auth.router, tags=["auth"])

@app.get("/")
def helloWorld():
    return {"hello": "world"}