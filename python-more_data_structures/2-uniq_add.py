#!/usr/bin/python3

def uniq_add(my_list=[]):
    int2 = 0
    for int3 in my_list:
        if my_list.count(int3) > 1:
            my_list.remove(int3)
    for int3 in my_list:
        int2 += int3
    return (int2)
