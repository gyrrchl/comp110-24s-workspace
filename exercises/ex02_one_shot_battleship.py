"""EX02 - One Shot Battleship."""

__author__ = "730475093"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size = 4
grid = f"{grid_size} by {grid_size}"

secret_row = 3
secret_column = 2

# Making sure the guess is in range
player_1_row = int(input("Guess a row: "))
while player_1_row > 4 or player_1_row < 1:
    player_1_row = int(input(f"The grid is only {grid}. Try again: "))

player_1_column = int(input("Guess a column: "))
while player_1_column > 4 or player_1_column < 1:
    player_1_column = int(input(f"The grid is only {grid}. Try again: "))

# Establishing results
result = ""
if player_1_row == secret_row and player_1_column == secret_column:
    result = RED_BOX
else:
    result = WHITE_BOX

# Building the grid
row_counter = 1
column_counter = 1

emoji_string = BLUE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX

while row_counter <= grid_size:
    emoji_string = ""
    while column_counter <= grid_size:
        if row_counter == player_1_row and column_counter == player_1_column:
            emoji_string += result
        else:
            emoji_string += BLUE_BOX
        column_counter += 1
    print(emoji_string)
    row_counter += 1
    column_counter = 1

# Hint conditions
if player_1_row == secret_row and player_1_column == secret_column:
    print("Hit!")
elif player_1_row == secret_row and player_1_column != secret_column:
    print("Close! Correct row, wrong column.")
elif player_1_row != secret_row and player_1_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
