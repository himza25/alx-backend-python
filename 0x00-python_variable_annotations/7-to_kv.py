#!/usr/bin/env python3
"""Module for creating a tuple with a string and the square of a number."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with a string and the square of a number (int or float).

    Args:
        k (str): The string component of the tuple.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of v.
    """
    return (k, float(v ** 2))
