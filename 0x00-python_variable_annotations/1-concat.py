#!/usr/bin/env python3
"""
a type-annotated function concat that takes a string str1 and
a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    '''A function that concatenates 2 strings'''
    return str1 + str2


if __name__ == '__main__':

    str1 = 'str1'
    str2 = 'str2'

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
