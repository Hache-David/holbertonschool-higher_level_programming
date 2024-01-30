#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0
    if len(tuple_a) == 1:
        int1 = 0
        int3 = tuple_a[0]
    elif len(tuple_a) == 0:
        int1 = 0
        int3 = 0
    else:
        int1 = tuple_a[1]
        int3 = tuple_a[0]
    if len(tuple_b) == 1:
        int2 = 0
        int4 = tuple_b[0]
    elif len(tuple_b) == 0:
        int2 = 0
        int4 = 0
    else:
        int2 = tuple_b[1]
        int4 = tuple_b[0]
    tuple_c = (int3 + int4, int1 + int2)
    print(tuple_c, end="")
    return ""
