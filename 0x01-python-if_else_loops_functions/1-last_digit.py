#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
lastdigit = abs(lastdigit)

if lastdigit > 5:
	print("Last digit of {} is {} and is greater than 5".format(number, lastdigit))
else:
	print("NULL")
