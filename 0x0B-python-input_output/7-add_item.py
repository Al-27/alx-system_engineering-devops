#!/usr/bin/python3
"""
    ...
"""
from sys import argv

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

fname = "add_item.json"

f = open(fname, "a+")
f.close()

obj = load(fname)
print(obj)
obj += argv[1:] 
save(obj,fname)