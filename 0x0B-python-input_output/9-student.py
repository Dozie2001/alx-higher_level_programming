#!/usr/bin/python3
"""A student defining class"""


class Student:
    """A class that shows what it means to be a student"""

    def __init__(self, first_name, last_name, age):
        """Initialisation of the parameters of a student
        args:
           first_name(str): The first name of the student
           last_name(str): The last name of the student
           age(int): The age of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dict representation of the class"""
        return self.__dict__
