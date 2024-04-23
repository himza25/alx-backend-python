#!/usr/bin/env python3
"""Modifies wait_n function to use task_wait_random for creating tasks."""
import asyncio
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """Executes n task_wait_random tasks and returns results."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
