#!/usr/bin/python3
def no_c(my_string):
    my_string.translate({ord('c'): None})
    my_string.translate({ord('C'): None})
    print('{:s}'.format(my_string))
