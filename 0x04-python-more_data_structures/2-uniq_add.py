#!/usr/bin/python3
def uniq_add(my_list=[]):
    value = 0
    for x in set(my_list):
        value += int(x)
    return value
