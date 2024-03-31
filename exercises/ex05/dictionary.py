"""Various Dictionary Exercises."""

__author__ = "730475093"


# invert
def invert(invert_dict: dict[str, str]) -> dict[str, str]:
    """Invert keys and values in dictionary."""
    inverted: dict[str, str] = {}
    for key, value in invert_dict.items():
        if value in inverted:
            raise KeyError("You made a key mistake!")
        inverted[value] = key
    return inverted


# favorite color
def favorite_color(colors: dict[str, str]) -> str:
    """Return most popular color as a string in a dictionary using a color counter."""
    color_count: dict[str, int] = {}
    most_pop_color = ""
    max_count = 0
    for color in colors.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 0
        
        if color_count[color] > max_count or (color_count[color] == max_count and color < most_pop_color):
            most_pop_color = color
            max_count = color_count[color]
    return most_pop_color


# count
def count(values: list[str]) -> dict[str, int]:
    """Count times item appears in list."""
    count_dict: dict[str, int] = {}
    for value in values:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict


# alphabetizer
def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetize list and return as dictionary."""
    alph_dict: dict[str, list[str]] = {}
    for word in words:
        if word and 'a' <= word[0].lower() <= 'z':
            letter1 = word[0].lower()

            if letter1 in alph_dict:
                alph_dict[letter1].append(word)
            else:
                alph_dict[letter1] = [word]

    return alph_dict
    

# update attendance
def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Im so tired and I need to go to sleep! But here is an attendance log for a hypothetical student."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]


test_dict: dict[str,int] = {"a": 2, "b": 4, "c": 7, "d": 1}
>>> test_val: int = 4
>>> value_exists(test_dict, test_val)
True
>>> value_exists(test_dict, 5)
False

test_dict: dict[str,int] = {"a": 2, "b": 4, "c": 7, "d": 1}
>>> test_val: int = 4
>>> plus_or_minus_n(test_dict, test_val)
>>> test_dict
{"a": 6, "b": 8, "c": 3, "d": -3}