from fastapi import FastAPI
from typing import List
from .models import User
from .crud import create_user, get_users, get_user, update_user, delete_user

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user_endpoint(user: User):
    return create_user(user)

@app.get("/users/", response_model=List[User])
def get_users_endpoint():
    return get_users()

@app.get("/users/{user_id}", response_model=User)
def get_user_endpoint(user_id: int):
    return get_user(user_id)

@app.put("/users/{user_id}", response_model=User)
def update_user_endpoint(user_id: int, updated_user: User):
    return update_user(user_id, updated_user)

@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int):
    return delete_user(user_id)
