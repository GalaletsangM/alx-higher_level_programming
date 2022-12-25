#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    counter = 1
    s = 0
    if length == 0:
        print('{:d}'.format(length))
    else:
        while counter <= length:
            s = s + int(sys.argv[counter])
            counter = counter + 1
        print('{:d}'.format(s))
