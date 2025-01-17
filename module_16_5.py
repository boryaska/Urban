from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users: List["User"] = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": None})

@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
    username: str = Path(..., min_length=5, max_length=20, description="Введите имя пользователя", example="UrbanUser"),
    age: int = Path(..., ge=18, le=120, description="Введите возраст", example=24)
) -> User:
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: int = Path(..., ge=1, le=1000, description="Введите ID пользователя", example=1),
    username: str = Path(..., min_length=5, max_length=20, description="Введите имя пользователя", example="UrbanUser"),
    age: int = Path(..., ge=18, le=120, description="Введите возраст", example=24)
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: int = Path(..., ge=1, le=1000, description="Введите ID пользователя", example=1)
) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    raise HTTPException(status_code=404, detail="User was not found")

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def user_detail(request: Request, user_id: int = Path(..., ge=1, le=1000, description="Введите ID пользователя", example=1)):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")