#!/usr/bin/python3
"""
 ......... .......... ..........
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo = main_url + "/user/{}/todos".format(argv[1])
    name = main_url + "/users/{}".format(argv[1])
    todo_rslt = get(todo).json()
    name_rslt = get(name).json()

    todo_num = len(todo_rslt)
    todo_cmplt = len([todo for todo in todo_rslt
                         if todo.get("completed")])
    name = name_rslt.get("name")
    print(f"Employee {name} is done with tasks({todo_cmplt}/{todo_num}):")
    for todo in todo_rslt:
        if (todo.get("completed")):
            print(f'\t {todo.get("title")}')