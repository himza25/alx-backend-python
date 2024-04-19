# Python Variable Annotations

This repository contains a series of tasks aimed at exploring the use of type annotations in Python, a feature available from Python 3.5 onwards. These tasks cover basic to advanced annotation techniques, including the use of `TypeVar`, duck typing, and complex type annotations.

## Tasks

### 0. Basic annotations - add
- **Description**: Write a type-annotated function `add` that takes two floats `a` and `b` as arguments and returns their sum as a float.

### 1. Basic annotations - concat
- **Description**: Create a type-annotated function `concat` that concatenates two strings `str1` and `str2` and returns the resulting string.

### 2. Basic annotations - floor
- **Description**: Develop a type-annotated function `floor` that takes a float `n` and returns the floor of the float as an integer.

### 3. Basic annotations - to string
- **Description**: Implement a type-annotated function `to_str` that converts a float `n` to its string representation.

### 4. Define variables
- **Description**: Define and annotate variables with specified values: an integer `a`, a float `pi`, a boolean `i_understand_annotations`, and a string `school`.

### 5. Complex types - list of floats
- **Description**: Write a function `sum_list` that takes a list of floats and returns their sum, using type annotations.

### 6. Complex types - mixed list
- **Description**: Create a function `sum_mixed_list` that handles a list of integers and floats, returning their sum as a float.

### 7. Complex types - string and int/float to tuple
- **Description**: Write a function `to_kv` that takes a string and either an int or float, returning a tuple consisting of the string and the square of the number as a float.

### 8. Complex types - functions
- **Description**: Develop a function `make_multiplier` that takes a float `multiplier` and returns a function that multiplies a float by this multiplier.

### 9. Let's duck type an iterable object
- **Description**: Annotate a function `element_length` that takes an iterable and returns a list of tuples, each containing an element from the iterable and its length.

### 10. Duck typing - first element of a sequence
- **Description**: Apply duck-typed annotations to enhance a function `safe_first_element` that returns the first element of a sequence or `None`.

### 11. More involved type annotations
- **Description**: Use `TypeVar` to add type annotations to a function `safely_get_value` that attempts to retrieve a value from a dictionary by key, or returns a default value.

### 12. Type Checking
- **Description**: Use `mypy` to validate and apply necessary changes to a function `zoom_array` that replicates elements of a tuple a specified number of times.

## Repository Details
- **GitHub repository**: alx-backend-python
- **Directory**: 0x00-python_variable_annotations

