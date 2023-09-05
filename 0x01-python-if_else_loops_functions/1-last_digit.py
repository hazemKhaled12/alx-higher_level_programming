#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def formatResult(number):
    lastDigit = int(str(number)[-1])
    if lastDigit > 5:
        return lastDigit, "greater than 5"
    if lastDigit == 0:
        return lastDigit, "0"
    if lastDigit < 6:
        return lastDigit, "less than 6 and not 0"


lastDigit, theString = formatResult(number)
print(f"Last digit of {number} is {lastDigit} and is {theString}")
