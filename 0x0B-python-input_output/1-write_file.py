#!/usr/bin/python3
"""
    write
"""

def write_file(filename="", text=""):
    """
    ...
    """
    
    if filename != "":
        with open(filename,"w+",encoding="utf-8") as f:
            f.write(text)
