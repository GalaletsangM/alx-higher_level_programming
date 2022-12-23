#!/usr/bin/python3
def remove_char(str, n):
    if n >= 0 and n < len(str):
        return (str.replace(str[n], ''))
    else:
        return (str)
