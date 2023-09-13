#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numn = 0
    denm = 0
    for t in my_list:
        numn += (t[1]*t[0])
        denm += t[1]
    return (numn/denm)
