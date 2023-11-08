#!/usr/bin/python3
def uniq_add(my_list=[]):
    da_list = set(my_list)
    num = 0
    for i in da_list:
        num += i
    return (num)
