#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        i.replace('c', '')
        i.replace('C', '')
    return my_string
