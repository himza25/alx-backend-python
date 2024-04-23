#!/usr/bin/env python3
"""
This module alters wait_n to use task_wait_random and creates a list of
completed task results.
"""

import asyncio
from 3-tasks import task_wait_random  # Adjust if different based on file setup


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Executes multiple task_wait_random tasks and returns a list of the results.

    Parameters:
    n (int): Number of tasks to spawn.
    max_delay (int): Maximum delay passed to task_wait_random.

    Returns:
    list: List of results from the completed tasks, in the order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = []
    for task in asyncio.as_completed(tasks):
        completed = await task
        completed_tasks.append(completed)
    return completed_tasks
