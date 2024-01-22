#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list[:]
    if idx < 0:
        return (a)
    if idx > len(my_list) - 1:
        return (a)
    a[idx] = element
    return (a)
