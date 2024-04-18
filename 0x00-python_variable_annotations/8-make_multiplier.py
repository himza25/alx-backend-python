#!/usr/bin/env python3
"""Module for creating a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create and return a function multiplies its input by a fixed number.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function multiplies its input`.
    """
    def multiplier_func(value: float) -> float:
        """Multiply the input value by the multiplier."""
        return value * multiplier
    return multiplier_func
