"""Splitting a dictionary into two lists."""


__author__ = "730475093"


def get_keys(key_dict: dict[str, int]) -> list[str]:
    """Create a list of present dictionary keys."""
    return list(key_dict.keys())


def get_values(value_dict: dict[str, int]) -> list[int]:
    """Create a list of present dictionary values."""
    return list(value_dict.values())