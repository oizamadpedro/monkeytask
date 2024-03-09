from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import task

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

@app.get("/")
def helloWorld():
    return {"hello": "world"}