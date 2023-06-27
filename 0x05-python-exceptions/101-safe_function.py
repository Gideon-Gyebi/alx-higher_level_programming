#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executing a function safely.
    Args:
        fct: Is the function to execute.
        args: Arguments for fct.
    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
        """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
