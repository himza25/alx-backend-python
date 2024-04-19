#!/usr/bin/env python3
'''
Module provides a function to replicate elements of a tuple.
'''

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Replicate each element in a tuple a given number of times.

    Args:
        lst (Tuple[Any, ...]): Tuple from which elements are replicated.
        factor (int): Number of times to replicate each element.

    Returns:
        List[Any]: List containing replicated elements.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


# Correct usage:
array = (12, 72, 91)  # Use a tuple instead of a list

zoom_2x = zoom_array(array)  # Correctly uses default factor

zoom_3x = zoom_array(array, 3)  # Use int type for factor
