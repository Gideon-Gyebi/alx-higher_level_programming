#!/usr/bin/python3

def safe_print_division(a, b):
    """a function that divides 2 integers (a & b) and prints the result"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
