"""List Utility Functions!"""

__author__ = "730475093"


# all
def all(numbers: list[int], indicated_number: int) -> bool:
    """Returns True if all numbers in the list are equal to the indicated number. Returns False if otherwise, or if the list is empty."""
    counter = 0
    while counter < len(numbers):
        if numbers[counter] != indicated_number:
            return False
        counter += 1
    return True if numbers else False


# max
def max(input: list[int]) -> int:
    """Returns the largest number in the list. Shows 'ValueError' if the list is empty."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_value = input[0]
    counter = 1
    while counter < len(input):
        if input[counter] > max_value:
            max_value = input[counter]
        counter += 1
    return max_value


# is equal
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Deep Equality. Returns True if every element at every index is equal in both lists; returns False if otherwise."""
    if len(list_1) != len(list_2):
        return False
    
    counter = 0
    while counter < len(list_1):
        if list_1[counter] != list_2[counter]:
            return False
        counter += 1
    return True


# extend
def extend(list_1: list[int], list_2: list[int]) -> None:
    """Mutates the first list by appending the second list's values to the end of it. Returns nothing."""
    counter = 0
    while counter < len(list_2):
        list_1.append(list_2[counter])
        counter += 1