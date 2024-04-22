#!/usr/bin/env python3
"""
Provides async functions to simulate random wait times up to a specified max.
"""

import asyncio
import random
from typing import float


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random time up to max_delay seconds.

    Args:
    max_delay (int): Maximum delay time in seconds. Defaults to 10.

    Returns:
    float: The actual delay time used.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
