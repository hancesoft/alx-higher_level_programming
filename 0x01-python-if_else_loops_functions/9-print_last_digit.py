#!/usr/bin/python3
# print last digit of number

def print_last_digit(number):
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return digit
