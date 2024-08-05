#!/usr/bin/env python3
import asyncio
"""
a module that defines a function to return a task
"""


def task_wait_random(n: int) -> asyncio.Task:
    """
    a function task_wait_random that takes an integer max_delay
    and returns a asyncio.Task
    """

    wait_random = __import__('0-basic_async_syntax').wait_random
    task = asyncio.create_task(wait_random(n))

    return task
