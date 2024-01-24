#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        z = len(my_list)
        total = 0
        for item in my_list:
            if item not in my_list[:-z]:
                total += item
            z -= 1
        return total
