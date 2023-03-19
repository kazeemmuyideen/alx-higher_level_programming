#!/usr/bin/python3
"""0-add_integer Module"""

def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a: first integer
        b: second integer

    Returns:
        addition of two integer
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
