#!/usr/bin/python3

def remove_char_at(str, n):
    newString = ''
    for index, char in enumerate(str):
        if index != n:
            newString += char

    return newString
