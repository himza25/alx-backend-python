#!/usr/bin/env python3
"""
Advanced type annotations using TypeVar for a generic type-safe retrieval
of a value from a dictionary.
"""

from typing import TypeVar, Mapping, Any, Optional

T = TypeVar('T')  # Type variable for a generic type


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """
    Retrieve a value from a dictionary by key or return default
    if key is not found.

    Args:
        dct (Mapping[Any, T]): Dictionary to retrieve the value.
        key (Any): Key to look for in the dictionary.
        default (Optional[T]): Default value if key not found.

    Returns:
        Optional[T]: Value from the dictionary or default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
