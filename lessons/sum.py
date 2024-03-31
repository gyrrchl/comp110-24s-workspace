"""Summing the elements of a list using different loops."""

__author__ = "730475093"

vals = [1.1, 0.9, 1.0]


def w_sum(vals: list[float]) -> float:
    # Use a while loop to sum list of values
    """While loop."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


result = w_sum(vals)
print(result)


def f_sum(vals: list[float]) -> float:
    # Use a for ... in ... loop to sum list of values
    """For...in... loop."""
    total = 0.0
    for value in vals:
        total += value
    return total


result = f_sum(vals)
print(result)


def f_range_sum(vals: list[float]) -> float:
    # Use a for ... in range (...) loop to sum list of values
    """For...in range(...) loop; I don't understand why we need comments and docstrings within the code, should they say different things?"""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total


result = f_range_sum(vals)
print(result)