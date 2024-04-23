#!/usr/bin/env python3
"""
This module modifies the wait_n function to use task_wait_random, dynamically
importing it and handling tasks to return results as they complete.
"""

import asyncio
import importlib

basic_async_syntax = importlib.import_module("0-basic_async_syntax")
task_wait_random = getattr(basic_async_syntax, 'task_wait_random')


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Spawns n tasks using the dynamically imported task_wait_random and returns
    the results of these tasks as they complete.

    Parameters:
    n (int): Number of tasks to spawn.
    max_delay (int): Maximum delay that can be used in task_wait_random.

    Returns:
    list: List of float values representing the completion times of the tasks,
          sorted by the order of their completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
