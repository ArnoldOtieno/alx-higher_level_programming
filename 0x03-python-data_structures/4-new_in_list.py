#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        a = my_list[:]
        return (a)
    if idx > len(my_list) - 1:
        b = my_list[:]
        return (b)
    my_list[idx] = element
    return (my_list)
