#!/usr/bin/env python3
import time
import asyncio
"""
a module that defines a time measure function
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """

    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    result = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
