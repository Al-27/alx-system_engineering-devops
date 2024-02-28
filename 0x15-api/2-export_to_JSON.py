#!/usr/bin/python3
"""___________________________________"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    todos = get(
        f"https://jsonplaceholder.typicode.com/user/{argv[1]}/todos").json()
    users = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}").json()

    l_todo = []
    for todo in todos:
        d_todo = {"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": users.get("username")}
        l_todo.append(d_todo)

    with open(f"{argv[1]}.json", 'w') as f:
        dump({argv[1]: l_todo}, f)
