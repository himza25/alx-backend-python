#!/usr/bin/env python3
"""
Extend functionality of wait_random to handle multiple instances concurrently.
"""

import asyncio
from typing import List

# Assuming the file has been renamed to zero_basic_async_syntax.py
from zero_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random() n times with specified max_delay

    Args:
    n (int): Number of concurrent wait_random calls.
    max_delay (int): Maximum delay for each call, in seconds.

    Returns:
    List[float]: Durations of each call
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
