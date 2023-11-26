#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    n = 0
    den = 0

    for x in my_list:
        n += x[0] * x[1]
        den += x[1]

    return (n / den)
