import os
from typing import List
from .models import User

DATA_FILE = "C:/Users/user/Music/fastapi-app/app/users.txt"

def read_users_from_file() -> List[User]:
    print(f"users file: {DATA_FILE}")
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        lines = file.readlines()
    users = []
    print("users:")
    for line in lines:
        user_data = line.strip().split(",")
        users.append(User(id=int(user_data[0]), name=user_data[1], email=user_data[2]))
    return users

def write_users_to_file(users: List[User]) -> None:
    with open(DATA_FILE, "w") as file:
        for user in users:
            file.write(f"{user.id},{user.name},{user.email}\n")
