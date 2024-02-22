#!/usr/bin/python3
'''Write a function that returns the JSON
representation of an object (string):'''

import json


def to_json_string(my_obj):
    '''to json'''
    return_obj = json.dumps(my_obj)
    return return_obj
