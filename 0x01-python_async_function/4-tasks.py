#!/usr/bin/env python3
from typing import List
"""
a module that defines asynchronous function
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. it will spawn wait_random n
    times with the specified max_delay.
    """

    task_wait_random = __import__('3-tasks').task_wait_random
    delay = []
    for i in range(0, n):
        delay.append(await task_wait_random(max_delay))

    return sorted(delay)
