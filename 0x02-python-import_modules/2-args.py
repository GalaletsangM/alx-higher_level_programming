#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        print('0 argumets.')
    for i in range(1, len(sys.argv)):
        if len(sys.argv) == 2:
            print('1 argument:')
        else:
            print('{:d} argumets:'.format(len(sys.argv) - 1))

        print('{:d}: {:s}'.format(i, sys.argv[i]))
