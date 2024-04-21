"""Standard to Recursive."""

__author__ = "730475093"


def f(n: int, k: int) -> int:
    """Creating a recursive function from a standard function."""
    # base case
    if n == 0:
        return 0
    # recursive case
    else:
        return n * k
