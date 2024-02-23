#!/usr/bin/python3
'''Write a function that creates an
Object from a “JSON file”'''

import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        file_str = f.read()
    return json.loads(file_str)
