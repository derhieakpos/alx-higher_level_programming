#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for num in my_list:
        if search == num:
            return[replace for num in my_list]
        else:
            return[num for num in my_list]
