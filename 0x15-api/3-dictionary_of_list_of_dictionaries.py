#!/usr/bin/python3
""" this a cursed documentation"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    users = get("https://jsonplaceholder.typicode.com/users").json()

    big_dict = {}
    for user in users:
        todo_list = []

        todo_r = get(
            f"https://jsonplaceholder.typicode.com/user/{user.get('id')}/todos").json()
        user_r = get(
            f"https://jsonplaceholder.typicode.com/users/{user.get('id')}").json()
        for todo in todo_r:
            todo_dict = {}
            todo_dict.update({"username": user_r.get("username"),
                              "task": todo.get("title"),
                              "completed": todo.get("completed")})
            todo_list.append(todo_dict)

        big_dict.update({user.get("id"): todo_list})

    with open("todo_all_employees.json", 'w') as f:
        dump(big_dict, f)
