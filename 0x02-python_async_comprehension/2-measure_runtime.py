#!/usr/bin/env python3
"""Module to measure runtime of async comprehensions executed in parallel."""
import asyncio
import time
from typing import Coroutine

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of executing async_comprehension."""
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()
    return end - start
