#!/usr/bin/env python3
"""Module to create asyncio tasks from the wait_random coroutine."""

import asyncio
from zero_basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task from the wait_random coroutine.

    Args:
    max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
    asyncio.Task: The asyncio.Task object created from the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
