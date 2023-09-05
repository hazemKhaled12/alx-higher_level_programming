#!/usr/bin/python3

def getLastDigit(number):
    if number >= 0:
        return number % 10
    else:
        return (number % -10) * -1


def print_last_digit(number):
    lastDigit = getLastDigit(number)
    print("{:d}".format(lastDigit), end="")
    return lastDigit
