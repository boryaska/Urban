from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import PlainTextResponse
from typing import Annotated

app = FastAPI()

# Используем числовые ключи для словаря
users = {1: 'Имя: Example, возраст: 18'}

@app.get("/users", response_class=PlainTextResponse)
async def get_users() -> str:
    return str(users)

@app.post(
    "/user/{username}/{age}",
    response_class=PlainTextResponse
)
async def create_user(
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Введите имя пользователя",
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            ge=18,
            le=120,
            description="Введите возраст",
            example=24
        )
    ]
) -> str:
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered"

@app.put(
    "/user/{user_id}/{username}/{age}",
    response_class=PlainTextResponse
)
async def update_user(
    user_id: Annotated[
        int,
        Path(
            ge=1,
            le=1000,
            description="Введите ID пользователя",
            example=1
        )
    ],
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Введите имя пользователя",
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            ge=18,
            le=120,
            description="Введите возраст",
            example=24
        )
    ]
) -> str:
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"The user {user_id} is updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete(
    "/user/{user_id}",
    response_class=PlainTextResponse
)
async def delete_user(
    user_id: Annotated[
        int,
        Path(
            ge=1,
            le=1000,
            description="Введите ID пользователя",
            example=1
        )
    ]
) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} deleted"