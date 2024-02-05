#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        for int in my_list:
            if index < x:
                print(int, end="")
                index += 1
    except IndexError:
        pass
    finally:
        print()
    return index
