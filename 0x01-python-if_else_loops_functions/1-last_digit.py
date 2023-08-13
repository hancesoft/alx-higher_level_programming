#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# lastdigit = int(repr(number)[-1])

lastdigit = abs(number) % 10

if lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastdigit))

negdigit = -lastdigt
elif negdigit:
    if negdigit and negdigit > -5:
        print("Last digit of {} is {} and is greater than 5".format(number, negdigit))
    elif negdigit == 0:
        print("Last digit of {} is {} and is 0".format(number, negdigit))
    elif negdigit < -6 and negdigit != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, negdigit))
