#!/usr/bin/python3
'''Write a class Student that defines a student '''


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return class to json'''
        new_dict = {}
        if (isinstance(attrs, list) and
                all(isinstance(element, str) for element in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
