from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory = 'templates')
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def req(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request':request, 'users': users})


@app.get("/user/{user_id}")
async def get_all_records(request: Request, user_id: int) -> HTMLResponse:
    for i in users:
        if i.id == user_id:
            return templates.TemplateResponse('users.html', {'request':request, 'user': i})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}')
async def add_data(username: str = Path(description='Enter Name', example='Victor'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='32')):
    superuser = User(id = (lambda ids, one: 1 if len(ids) == 0 else ids[-1].id+one)(users, 1),username=username, age=age)
    users.append(superuser)
    return superuser

@app.put('/user/{user_id}/{username}/{age}')
async def update_data(user_id: int = Path(ge=1, description='Enter ID',example='3'),
                      username: str = Path(description='Enter Name', example='Victor'),
                      age: int = Path(ge=18, le=120, description='Enter age', example='32')):
    for i in users:
        if i.id == user_id:
            i.username = username
            i.age = age
            return i
    raise HTTPException(status_code=404, detail="User was not found")



@app.delete('/user/{user_id}')
async def delete_data(user_id: int = Path(ge=1, description='Enter ID',example='3')):
    for i in users:
        if i.id == user_id:
            users.remove(i)
            return i
    raise HTTPException(status_code=404, detail="User was not found")


