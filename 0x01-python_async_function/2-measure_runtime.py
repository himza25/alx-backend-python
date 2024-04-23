#!/usr/bin/env python3
"""Measure runtime of async coroutine wait_n."""
import time
import asyncio
from typing import List
from one_concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure average time per execution of wait_n.
    Args:
    n (int): Number of executions.
    max_delay (int): Max delay per execution.
    Returns:
    float: Average time per execution.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
