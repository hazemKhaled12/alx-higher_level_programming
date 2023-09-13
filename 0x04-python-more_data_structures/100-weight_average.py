#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    i = 1
    numn = 0
    denm = 0
    for t in my_list:
        numn += (t[1]*i)
        denm += t[1]
        i += 1
    return (numn/denm)
