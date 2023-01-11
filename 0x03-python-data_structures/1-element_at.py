#!/usr/bin/python3

def element_at(my_list, idx):
    # a function that replaces an element of a list at a specific position
    # (like in C).

    if idx < 0 or idx > (len(my_list) - 1):
        return 'none'
    else:
        return(my_list[idx])