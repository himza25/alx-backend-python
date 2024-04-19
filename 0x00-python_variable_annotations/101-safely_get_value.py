#!/usr/bin/env python3
'''
Advanced type annotations using TypeVar for a generic type-safe retrieval
of a value from a dictionary.
'''

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')  # Declare type variable


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieve a value from a dictionary by key or return default if
    the key is not found.

    Args:
        dct (Mapping[Any, T]): Dictionary from which to retrieve the value.
        key (Any): Key to look for in the dictionary.
        default (Union[T, None]): Default value if key not found.

    Returns:
        Union[Any, T]: Value from the dictionary or default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
