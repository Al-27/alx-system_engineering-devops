#!/usr/bin/python3
"""
    append
"""

def append_write(filename="", text=""):
    """
    ...
    """
    if filename != "":
        with open(filename,"a+",encoding="utf-8") as f:
            f.touch(exist_ok=True) 
            f.write(text)
