#!/usr/bin/env python3
"""
Module for getting a value from a dictionary safely with
advanced type annotations.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')  # Declare type variable


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """
    Retrieve a value from a dictionary by key or return default
    if key is not found.

    Args:
        dct (Mapping[Any, T]): Dictionary to retrieve the value.
        key (Any): Key to look for in the dictionary.
        default (Union[T, None], optional): Default value if key not found.
        Defaults to None.

    Returns:
        Union[T, None]: Value from the dictionary or default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
