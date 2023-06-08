#!/usr/bin/python3
def remove_char_at(str, n):
    """Creating a copy of a string
    without the character at "n" position."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
