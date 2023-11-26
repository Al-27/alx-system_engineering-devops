#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for x in keys:
        if value == a_dictionary.get(x):
            del a_dictionary[x]

    return (a_dictionary)
