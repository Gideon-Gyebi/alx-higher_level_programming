#!/usr/bin/python3
"""This defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsenting base geometry."""

    def area(self):
        """Is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating a parameter as an integer.

        Args:
            name (str): Is the name of the parameter.
            value (int): Is the parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
