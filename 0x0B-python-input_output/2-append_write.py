#!/usr/bin/python3
"""
    append
"""

def append_write(filename="", text=""):
    """
    ...
    """
    
    if filename != "":
        with open(filename,"aw",encoding="utf-8") as f:
            f.write(text)