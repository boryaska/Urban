from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def main_page() -> str:
    return "Главная страница"

@app.get("/user/admin", response_class=PlainTextResponse)
async def admin_page() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}", response_class=PlainTextResponse)
async def user_page(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user", response_class=PlainTextResponse)
async def user_info(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"



