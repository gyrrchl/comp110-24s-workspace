
"""CQ08 OOP practice."""

from __future__ import annotations


class Point:
    """Creating a class for the object Point."""

    # attributes
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initializing x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutate: multiply x and y coordinates by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Multiply x and y coordinates by factor and return new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point