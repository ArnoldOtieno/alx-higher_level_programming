#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpMylist = my_list[:]
    cnt = 0
    for item in my_list:
        if item == search:
            cpMylist[cnt] = replace
        cnt += 1
    return cpMylist
