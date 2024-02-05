#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list[:x]:
            count += 1
            print("{}".format(item), end="")
        print()
        return count
    except IndexError:
        print("Out of index")
