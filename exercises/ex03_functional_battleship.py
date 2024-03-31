"""Functional Battleship!"""

__author__ = "730475093"

import random


def input_guess(grid_size: int, grid_specification: str) -> int:
    """User inputs guess."""
    assert grid_specification == "row" or grid_specification == "column"
    attempt = 0
    while True:
        if attempt == 0:
            if grid_specification == "row":
                guess = int(input("Guess a row: "))
            else:
                guess = int(input("Guess a column: "))
        else:
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        if 1 <= guess <= grid_size:
            return guess
        attempt += 1


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    """Prints Grid using guess cell."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: str = ""
    row_counter: int = 1
    if correct_guess:
        result = RED_BOX
    else:
        result = WHITE_BOX
    while row_counter <= grid_size:
        row_str: str = ""
        column_counter: int = 1
        while column_counter <= grid_size:
            if column_guess == column_counter and row_guess == row_counter:
                row_str += result
            else:
                row_str += BLUE_BOX
            column_counter += 1
        print(row_str)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Checks if secret location matches guess location."""
    return secret_row == row_guess and secret_column == column_guess


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Runs main loop."""
    turn_counter: int = 0
    turn_max: int = 5
    win: bool = False
    while turn_counter < turn_max and not win:
        turn_counter += 1
        print(f"=== Turn {turn_counter}/{turn_max} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        the_correct_guess = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, the_correct_guess)
        if the_correct_guess:
            print(f"Hit! You won in {turn_counter}/{turn_max} turns!")
            win = True
        else:
            print("Miss!")         
    if not win:
        print(f"X/{turn_max} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))