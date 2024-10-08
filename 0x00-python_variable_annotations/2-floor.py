#!/usr/bin/env python3
"""
a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""


def floor(n: float) -> int:
    '''a function that reduces a float to an integer'''
    return int(n)


if __name__ == '__main__':
    import math

    ans = floor(3.14)

    print(floor(3.14))
    print(floor(38.14))
    print(floor(38.143))
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
