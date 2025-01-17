from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

users: List["User"] = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:

    return users

@app.post("/user/{username}/{age}", response_model=User)
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
) -> User:

    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
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
) -> User:

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
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
) -> User:

    for index, user in enumerate(users):
        if user.id == user_id:
            removed_user = users.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail="User was not found")