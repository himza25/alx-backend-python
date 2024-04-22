#!/usr/bin/env python3
"""
This module extends the functionality of the wait_random coroutine to handle
multiple instances concurrently and return results in the order of completion.
"""

import asyncio
from typing import List

# Ensure that wait_random is accessible from the module '0-basic_async_syntax'
from 0_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random() n times with the specified max_delay.

    Args:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay in seconds for each wait_random call.

    Returns:
    List[float]: A list of delay durations from each wait_random call,
                 returned in the order they were completed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
