# Python Async Comprehensions

This repository features Python scripts demonstrating the application of asynchronous programming using comprehensions and generators in Python 3.7, designed to execute in an Ubuntu 18.04 LTS environment.

## Repository Structure

Here are the tasks included in the `0x02-python_async_comprehension` directory:

### Task 0: Async Generator

**File:** `0-async_generator.py`

- Implements a coroutine called `async_generator` which takes no arguments.
- Loops 10 times, each time asynchronously waiting for 1 second, then yields a random number between 0 and 10.

### Task 1: Async Comprehensions

**File:** `1-async_comprehension.py`

- Uses a coroutine, `async_comprehension`, that imports and utilizes `async_generator` from Task 0.
- Collects and returns 10 random numbers using an async comprehension.

### Task 2: Run Time for Four Parallel Comprehensions

**File:** `2-measure_runtime.py`

- Contains a coroutine `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`.
- Measures and returns the total runtime, highlighting the asynchronous execution efficiency.

## Additional Information

- Each script adheres strictly to PEP8 styling with detailed docstrings and type annotations.
- Ensure Python 3.7 is used for testing to match the execution environment specifications.
