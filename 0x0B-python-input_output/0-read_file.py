#!/usr/bin/python3
"""
    read
"""

def read_file(filename=""):
    """
        ...
    """
    fn = filename
    if fn != "":
        with open(fn,encoding="utf-8") as f:
            for line in f:
                print(line,end='')

    