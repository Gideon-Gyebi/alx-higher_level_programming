#!/usr/bin/python3
"""This defines a class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): Is the first name of the student.
            last_name (str): Is the last name of the student.
            age (int): Is the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Getting a dictionary representation of the Student."""
        return self.__dict__
