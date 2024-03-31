"""Dictionary Unit Tests!"""

__author__ = "730475093"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

# invert unit tests


def test_invert_1() -> None:
    """Invert unit test; use case #1."""
    invert_dict: dict[str, str] = {"geyer": "rachel"}
    assert invert(invert_dict) == {"rachel": "geyer"}


def test_invert_2() -> None:
    """Invert unit test; use case #2."""
    invert_dict: dict[str, str] = {"chapel": "hill", "nc": "state", "western": "carolina"}
    assert invert(invert_dict) == {"hill": "chapel", "state": "nc", "carolina": "western"}


def test_invert_3() -> None:
    """Invert unit test; edge case #1."""
    invert_dict: dict[str, str] = {"mac": "book", "chrome": "bookk"}
    assert invert(invert_dict) == {"book": "mac", "bookk": "chrome"}


# favorite color unit tests

def test_favorite_color_1() -> None:
    """Favorite color unit test; use case #1."""
    colors: dict[str, str] = {"Rachel": "green", "Sarah": "green", "Kevin": "orange"}
    assert favorite_color(colors) == "green"


def test_favorite_color_2() -> None:
    """Favorite color unit test; use case #2."""
    colors: dict[str, str] = {"UNC": "blue", "Duke": "blue", "Wilmington": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_3() -> None:
    """Favorite color unit test; edge case #1."""
    colors: dict[str, str] = {}
    # should return nothing because an empty dictionary is given
    assert favorite_color(colors) == ""


# count unit tests

def test_count_1() -> None:
    """Count unit test; use case #1."""
    values: list[str] = ["latte", "latte", "americano"]
    assert count(values) == {"latte": 2, "americano": 1}


def test_count_2() -> None:
    """Count unit test; use case #2."""
    values: list[str] = ["78", "79", "72"]
    assert count(values) == {"78": 1, "79": 1, "72": 1}


def test_count_3() -> None:
    """Count unit test; edge case #1."""
    values: list[str] = ["clover", "clover", "clover", "clover", "clover", "clover", "clover", "clover"]
    # using many more inputs than usual in the list?
    assert count(values) == {"clover": 8}


# alphabetizer unit tests

def test_alphabetizer_1() -> None:
    """Alphabetizer unit test; use case #1."""
    words: list[str] = ["coconut", "apricot", "boisenberry"]
    assert alphabetizer(words) == {"a": ["apricot"], "b": ["boisenberry"], "c": ["coconut"]}


def test_alphabetizer_2() -> None:
    """Alphabetizer unit test; use case #2."""
    words: list[str] = ["mosquito", "stick bug", "spider"]
    assert alphabetizer(words) == {"m": ["mosquito"], "s": ["stick bug", "spider"]}


def test_alphabetizer_3() -> None:
    """Alphabetizer unit test; edge case #1."""
    words: list[str] = ["Jinx", "Jade", "Jeffita"]
    # all words will be alphabetized into j, but values will not be alphabetized within the j key
    assert alphabetizer(words) == {"j": ["Jinx", "Jade", "Jeffita"]}

# update attendance unit tests


def test_update_attendance_1() -> None:
    """Update attendance unit test; use case #1."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Davis", "Bacot"]}
    day: str = "Monday"
    student: str = "Cadeu"
    # adding Cadeu to the Monday attendance log
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"Monday": ["Davis", "Bacot", "Cadeu"]}


def test_update_attendance_2() -> None:
    """Update attendance unit test; use case #2."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vivi", "Jinx"], "Tuesday": ["Jade"]}
    day: str = "Tuesday"
    student: str = "Jeffita"
    # adding Jeffita to the Tuesday attendance log
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"Monday": ["Vivi", "Jinx"], "Tuesday": ["Jade", "Jeffita"]}


def test_update_attendance_3() -> None:
    """Update attendance unit test; edge case #1."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Septer"], "Tuesday": ["Moore"]}
    day: str = "Wednesday"
    student: str = "Linden"
    # adding Linden to new day, Wednesday, in attendance log
    update_attendance(attendance_log, day, student)
    assert attendance_log == {"Monday": ["Septer"], "Tuesday": ["Moore"], "Wednesday": ["Linden"]}