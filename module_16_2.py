from fastapi import FastAPI, Path
app = FastAPI()

@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_ids(user_id: int = Path(gt=1, le=100, description = 'Enter User ID', example='66')):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def users_info(username: str = Path(min_length=5, max_length=20, description='Enter username', example='Victor'),
                     age: int = Path(ge=18, le=120, description='Enter age', example='32')):
    return f"Информация о пользователе. Имя {username}, Возраст:{age}"


@app.get("/")
async def welcome():
    return "Главная страница"
