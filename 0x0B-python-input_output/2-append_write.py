#!/usr/bin/python3
"""
    append
"""

def append_write(filename="", text=""):
    """
    ...
    """
    f = Path(filename)
    f.touch(exist_ok=True) 
    if filename != "":
        with open(filename,"a+",encoding="utf-8") as f:
            f.write(text)
