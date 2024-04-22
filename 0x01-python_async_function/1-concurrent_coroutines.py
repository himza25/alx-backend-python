#!/usr/bin/env python3
"""
Extend wait_random to handle multiple instances concurrently, returning results by completion.
"""

import asyncio
from typing import List

# Adjusting the module name for correct Python syntax
from zero_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random() n times with max_delay, returns durations as completed.

    Args:
    n (int): Number of wait_random instances.
    max_delay (int): Max delay for each wait_random.

    Returns:
    List[float]: Durations from wait_random, ordered by completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
