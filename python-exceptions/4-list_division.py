#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            if isinstance(my_list_1[i], int) and isinstance(my_list_2[i], int):
                if my_list_2[i] == 0:
                    raise ZeroDivisionError
                new_list.append(my_list_1[i] / my_list_2[i])
            else:
                raise TypeError
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
        finally:
            pass
    return new_list
