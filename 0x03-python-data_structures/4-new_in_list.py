#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    new_list = my_list[:]

    if idx < 0 or idx > len(my_list):
        return None
    new_list[idx] = new_element

    return new_list
