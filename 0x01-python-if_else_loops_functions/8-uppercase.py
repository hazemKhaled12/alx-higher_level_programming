#!/usr/bin/python3
def islower(c):
    if ord(c) in range(ord("a"), ord("z")):
        return True
    else:
        return False


def uppercase(s):
    for char in s:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            print("{:c}"
                  .format(ord(char) if not islower(char) else ord(char) - 32),
                  end="")


print()
