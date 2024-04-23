#!/usr/bin/env python3
"""Module to measure average runtime of the wait_n coroutine."""
from time import time
import asyncio
from one_concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of the wait_n coroutine.

    Args:
    n (int): Number of coroutine executions.
    max_delay (int): Maximum delay for wait_n.

    Returns:
    float: Average time per coroutine execution.
    """
    initial_time = time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time() - initial_time
    return total_time / n
