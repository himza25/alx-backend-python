#!/usr/bin/env python3
"""Module to measure average runtime of the wait_n coroutine."""
from time import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time of the wait_n coroutine."""
    initial_time = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - initial_time) / n
