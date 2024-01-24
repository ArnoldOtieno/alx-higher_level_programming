#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        z = len(my_list)
        sum = 0
        for item in my_list:
            if item not in my_list[:-z]:
                sum += item
            z -= 1
        return sum
