from typing import List
from fastapi import HTTPException
from .models import User
from .storage import read_users_from_file, write_users_to_file

def create_user(user: User) -> User:
    users = read_users_from_file()
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User with this ID already exists.")
    users.append(user)
    write_users_to_file(users)
    return user

def get_users() -> List[User]:
    return read_users_from_file()

def get_user(user_id: int) -> User:
    users = read_users_from_file()
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found.")

def update_user(user_id: int, updated_user: User) -> User:
    users = read_users_from_file()
    for idx, user in enumerate(users):
        if user.id == user_id:
            users[idx] = updated_user
            write_users_to_file(users)
            return updated_user
    raise HTTPException(status_code=404, detail="User not found.")

def delete_user(user_id: int):
    users = read_users_from_file()
    for idx, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(idx)
            write_users_to_file(users)
            return {'result': 'user deleted successfully'}
    raise HTTPException(status_code=404, detail="User not found.")
