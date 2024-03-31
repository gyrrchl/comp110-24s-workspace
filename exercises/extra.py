  if row_counter == 1:
        row_number = 1
    elif row_counter == 2:
        row_number = 2
    elif row_counter == 3:
        row_number = 3
    elif row_counter == 4:
        row_number = 4
    if column_counter == 1:
        column_number = 1
    elif column_counter == 2:
        column_number = 2
    elif column_counter == 3:
        column_number = 3
    elif column_counter == 4:
        column_number = 4
    if row_number == secret_row and column_number == secret_column:
        print(result)
    else:
        print(result)

while column_counter <= grid_size:
        if row_counter == player_1_row and column_counter == player_1_column:
            emoji_string += RED_BOX
        else:
         emoji_string += BLUE_BOX

   if row_counter == player_1_row:
        while column_counter <= grid_size:
            if column_counter == player_1_column:
                emoji_string += result
            else:
                emoji_string += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= grid_size:
            emoji_string += BLUE_BOX
            column_counter += 1
        print(emoji_string)
        row_counter += 1

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

while row_counter <= grid_size:
    print(emoji_string)
    row_counter += 1
    column_counter += 1