#!/usr/bin/env python3
"""
Execute multiple wait_random coroutines concurrently and return in .
"""

import asyncio
from typing import List

from zero_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random() n times with max_delay, return delays as completed.

    Args:
    n (int): Number of wait_random instances.
    max_delay (int): Max delay for each call in seconds.

    Returns:
    List[float]: Delays from wait_random, ordered by completion.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
