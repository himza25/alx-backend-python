#!/usr/bin/env python3
"""
This module imports wait_random and defines task_wait_random to return an
asyncio.Task.
"""

import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that executes wait_random with the provided
    max_delay.

    Parameters:
    max_delay (int): The maximum delay for the wait_random function.

    Returns:
    asyncio.Task: The created asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))
