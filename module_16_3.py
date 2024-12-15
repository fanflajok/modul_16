from fastapi import FastAPI, Path
app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def get_all_records():
    return users


@app.post('/user/{username}/{age}')
async def add_data(username: str = Path(description='Enter Name', example='Victor'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='32')):
    curr_index = str(int(max(users,key=int)) + 1)
    users[curr_index] = f'Имя: {username}, возраст: {age}'
    return f'User {curr_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_data(user_id: int = Path(description='Enter ID',example='3'), username:
str = Path(description='Enter Name', example='Victor'), age: int = Path(ge=18, le=120, description='Enter age', example='32')):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.post('/user/{user_id}')
async def delete_data(user_id: int):
    users.pop(str(user_id))
    return users


