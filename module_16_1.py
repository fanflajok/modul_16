from fastapi import FastAPI

app = FastAPI()

@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_ids(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def users_info(username: str, age: int):
    return f"Информация о пользователе. Имя {username}, Возраст:{age}"


@app.get("/")
async def welcome():
    return "Главная страница"



