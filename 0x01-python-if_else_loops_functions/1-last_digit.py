#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_digit = int(('-' * (number < 0)) + str(number)[-1])
print('Lst digit of {:d} is {:d} {:s}{:s}{:s}'.format(number, last_digit,
    'and is greater than 5' * (last_digit > 5),
    'and is 0' * (last_digit == 0),
    'and is less than 6 and not 0' * ((last_digit < 6) and (last_digit != 0))
    ))
