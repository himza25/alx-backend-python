#!/usr/bin/env python3
"""Module to concurrently execute multiple wait_random coroutines."""

import asyncio
from typing import List
from zero_basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random() n times with max_delay

    Args:
    n (int): Number of wait_random calls to execute.
    max_delay (int): Maximum delay for each wait_random call.

    Returns:
    List[float]: Sorted list of wait times as each call completes.
    """
    results = []
    for _ in range(n):
        results.append(await wait_random(max_delay))
    return sorted(results)
