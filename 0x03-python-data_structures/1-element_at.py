#!/usr/bin/python3
def element_at(my_list, idx):
    '''function that retrives an element from a like'''
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
