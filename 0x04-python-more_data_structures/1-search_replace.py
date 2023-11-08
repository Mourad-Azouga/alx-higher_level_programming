#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in range(len(my_list)):
        if search == new[i]:
            new[i] = replace
    return(new)
