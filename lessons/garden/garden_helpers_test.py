"""Test my garden functions."""


__author__ = "730475093"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_use() -> None:
    """Use case test for add by kind."""
    garden: dict[str, list[str]] = {"flowers": ["iris", "pansy"]}
    new_plant_kind: str = "flowers"
    new_plant: str = "rose"
    # adding rose to the list of flowers
    add_by_kind(garden, new_plant_kind, new_plant)
    assert garden == {"flowers": ["iris", "pansy", "rose"]}


def test_add_by_kind_edge() -> None:
    """Edge case test for add by kind."""
    garden: dict[str, list[str]] = {"flowers": ["iris", "pansy"]}
    new_plant_kind: str = "herbs" 
    # I think this would be an edge case test because instead of adding to current list, I'm adding a new list. I can't think of anything more specific to test.
    new_plant: str = "rosemary"
    # adding a new list, herbs, and adding rosemary to the list
    add_by_kind(garden, new_plant_kind, new_plant)
    assert garden == {"flowers": ["iris", "pansy"], "herbs": ["rosemary"]}


def test_add_by_date_use() -> None:
    """Use case test for add by date."""
    garden: dict[str, list[str]] = {"September": ["apples", "peas"]}
    month: str = "September"
    plant: str = "turnips"
    # adding turnips to list of plants in September
    add_by_date(garden, month, plant)
    assert garden == {"September": ["apples", "peas", "turnips"]}


def test_add_by_date_edge() -> None:
    """Edge case test for add by date."""
    garden: dict[str, list[str]] = {"September": ["apples", "peas"], "October": ["pumpkins", "squash"]}
    month: str = "November"
    plant: str = "corn"
    # adding a new list, November, and adding corn to the list. edge b/c November is a new list added to a set of two existing lists.
    add_by_date(garden, month, plant)
    assert garden == {"September": ["apples", "peas"], "October": ["pumpkins", "squash"], "November": ["corn"]}


def test_lookup_by_kind_and_date_use() -> None:
    """Use case test for lookup by kind and date."""
    kind_list: dict[str, list[str]] = {"fruit": ["lemons", "limes"]}
    month_list: dict[str, list[str]] = {"June": ["lemons", "strawberries"]}
    kind: str = "fruit"
    month: str = "June"
    # target kind is fruit and target date is June for creating the combined list
    lookup_by_kind_and_date(kind_list, month_list, kind, month)
    assert f"{kind}s to plant in {month}: ['lemons']" == lookup_by_kind_and_date(kind_list, month_list, kind, month)


def test_lookup_by_kind_and_date_edge() -> None:
    """Edge case test for lookup by kind and date."""
    kind_list: dict[str, list[str]] = {"fruit": ["lemons", "limes"]}
    month_list: dict[str, list[str]] = {"June": ["oranges", "strawberries"]}
    kind: str = "fruit"
    month: str = "June"
    # target kind is fruit and target date is June, but no combined list should be returned because there are no similarities between fruit and June. Instead, "else" message should appear.
    lookup_by_kind_and_date(kind_list, month_list, kind, month)
    assert f"No {kind}s to plant in {month}." == lookup_by_kind_and_date(kind_list, month_list, kind, month)