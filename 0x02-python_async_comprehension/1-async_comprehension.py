#!/usr/bin/env python3
"""Module to collect random numbers using an async generator."""
from typing import List

async_comprehension = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using a comprehension."""
    return [i async for i in async_comprehension()]
