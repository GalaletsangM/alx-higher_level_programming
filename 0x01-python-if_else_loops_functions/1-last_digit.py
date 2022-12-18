#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastdigit1 = number % 10
    if lastdigit1 > 5:
        print('Last digit of', number, 'is', lastdigit1, 
                'and is greater than 5')
    elif lastdigit1 == 0:
        print('last digit of', number, 'is', lastdigit1, 'and is 0')
    elif lastdigit1 < 6 and lastdigit1 != 0:
        print('Last digit of', number, 'is', lastdigit1, 
                'and is less than 6 and not 0')
else:
    lastdigit = number % -10
    if lastdigit > -5:
        print('Last digit of', number, 'is', lastdigit, 
                'and is greater than 5')
    elif lastdigit == 0:
        print('last digit of', number, 'is', lastdigit, 'and is 0')
    elif lastdigit < -6 and lastdigit != '0':
        print('Last digit of', number, 'is', lastdigit, 
                'and is less than 6 and not 0')
