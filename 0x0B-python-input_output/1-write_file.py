#!/usr/bin/python3
"""
    write
"""

def write_file(filename="", text=""):
    """
    ...
    """
    
    if filename != "":
        with open(filename,"w+") as f:
            f.write(text)
