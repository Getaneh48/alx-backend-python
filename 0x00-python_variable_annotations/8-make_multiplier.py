#!/usr/bin/env python3
from typing import Callable
"""
a type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by a float'''
    return lambda k: k * multiplier


if __name__ == '__main__':
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
