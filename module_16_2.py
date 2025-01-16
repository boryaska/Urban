from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse
from typing import Annotated

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def main_page() -> str:
    return "Главная страница"

@app.get("/user/admin", response_class=PlainTextResponse)
async def admin_page() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}", response_class=PlainTextResponse)
async def user_page(
    user_id: Annotated[
        int,
        Path(
            ge=1,
            le=100,
            description="Enter User ID",
            example=1
        )
    ]
) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}", response_class=PlainTextResponse)
async def user_info(
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            ge=18,
            le=120,
            description="Enter age",
            example=24
        )
    ]
) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"