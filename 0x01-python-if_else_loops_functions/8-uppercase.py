#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            print("{:s}".format(chr(ord(char) - 32)), end="")
        else:
            print("{:s}".format(char), end="")


print()
