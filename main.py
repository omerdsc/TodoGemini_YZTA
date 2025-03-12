from fastapi import FastAPI,Request
from fastapi.staticfiles import  StaticFiles
from setuptools.extern import names
from starlette.responses import RedirectResponse
from starlette import status
from models import Base
from database import engine
from routers.auth import router as auth_router #routere ekliyoruz
from routers.todo import router as todo_routher

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.get("/")
def read_root(request:Request):
    return RedirectResponse(url="/todo/todo-page",status_code=status.HTTP_302_FOUND)

app.include_router(auth_router)#routera ekliyoruz
app.include_router(todo_routher)

Base.metadata.create_all(bind=engine)
