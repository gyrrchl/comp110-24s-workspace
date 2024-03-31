"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730475093"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Convert input to an integer
player_1 = int(input("Pick a secret boat location between 1 and 4:"))

if player_1 > 4:
    print(f"Error! {player_1} too high!")     
    exit()
elif player_1 < 1:
    print(f"Error! {player_1} too low!")
    exit()

player_2 = int(input("Guess a number between 1 and 4:"))

if player_2 > 4:
    print(f"Error! {player_2} too high!")
    exit()
elif player_2 < 1:
    print(f"Error! {player_2} too low!")
    exit()

emoji_string = BLUE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX

if player_1 == player_2:
    result = RED_BOX
    print("Correct! You hit the ship.")
else:
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")

if player_2 == 1:
    emoji_string = result + emoji_string[1] + emoji_string[2] + emoji_string[3]
elif player_2 == 2:
    emoji_string = emoji_string[0] + result + emoji_string[2] + emoji_string[3]
elif player_2 == 3:
    emoji_string = emoji_string[0] + emoji_string[1] + result + emoji_string[3]
elif player_2 == 4:
    emoji_string = emoji_string[0] + emoji_string[1] + emoji_string[2] + result

print(emoji_string)