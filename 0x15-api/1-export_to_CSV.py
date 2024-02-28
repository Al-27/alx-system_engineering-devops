#!/usr/bin/python3
"""this is a documentation"""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == "__main__":
    todos = get(f"https://jsonplaceholder.typicode.com/user/{argv[1]}/todos").json()
    users = get(f"https://jsonplaceholder.typicode.com/user/{argv[1]}").json()

    todo_list = []
    for todo in todos:
        todo_dict = {}
        todo_dict.update({"user_ID": argv[1], "username": users.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        todo_list.append(todo_dict)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(todo_list)