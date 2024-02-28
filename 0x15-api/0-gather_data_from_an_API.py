#!/usr/bin/python3
"""
 ......... .......... ..........
"""

from requests import get
from sys import argv

if __name__ == '__main__': 
    todo_rslt = get(f'https://jsonplaceholder.typicode.com/user/{argv[1]}/todos').json()
    user = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}').json()

    todo_num = len(todo_rslt)
    cmp_todo = []
    for td in todo_rslt:
        if td.get("completed"):
            cmp_todo.append(td.get("title"))
    name = user.get("name")
    print(f"Employee {name} is done with tasks({len(cmp_todo)}/{todo_num}):")
    for todo in cmp_todo:
        print(f'\t {todo}')