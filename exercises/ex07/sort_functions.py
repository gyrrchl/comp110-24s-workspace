"""Functions that implement sorting algorithms."""

__author__ = "730475093"


# Part 1. Implementing Sort Algorithms

# 1a. Selection Sort

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sort_index: int = 0
    while sort_index < len(x) - 1:
        unsorted_index: int = sort_index + 1
        # moving backwards, compare the current element to all elements in the sorted part of the list and make swaps as you go
        while unsorted_index > 0 and x[unsorted_index] < x[unsorted_index - 1]:
            temp: int = x[unsorted_index]
            x[unsorted_index] = x[unsorted_index - 1]
            x[unsorted_index - 1] = temp
            # decrement the unsorted index variable
            unsorted_index -= 1
        sort_index += 1
    return None


# 1b. Insertion Sort

def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    counter: int = 0
    while counter < len(x):
        # find index of min element in only unsorted portion
        min_index: int = counter
        for min_elem in range(counter, len(x)):
            if x[min_elem] < x[min_index]:
                min_index = min_elem
        # compare min element and current element
        if min_index != counter:
            temp: int = x[counter]
            x[counter] = x[min_index]
            x[min_index] = temp
        counter += 1
    return None