#!/usr/bin/python3

"""Printing the alphabet in lowercase, and not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
