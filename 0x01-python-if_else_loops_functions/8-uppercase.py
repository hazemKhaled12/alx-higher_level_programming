#!/usr/bin/python3
def check(char):
    if not (ord(char) >= ord("a") and ord(char) <= ord("z")):
        return ord(char)
    else:
        return (ord(char) - 32)


def uppercase(s):
    for char in s:
        print("{:c}".format(check(char)), end="")
    print()
