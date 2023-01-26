#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = 0
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {:d}".format(res))
        return res
