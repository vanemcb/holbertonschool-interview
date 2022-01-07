#!/usr/bin/python3
"""
Method minOperations
"""


def minOperations(n):

    if type(n) is not int or n <= 0:
        return 0

    oper = 0
    char = 1
    copy = 1

    while char < n:
        if n % char == 0:
            copy = char
            oper += 1
        if char != n:
            char += copy
            oper += 1
        else:
            break

    return oper
