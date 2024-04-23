#!/usr/bin/env python3
"""Module that generates random numbers asynchronously."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates 10 random numbers between 0 and 10 asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
