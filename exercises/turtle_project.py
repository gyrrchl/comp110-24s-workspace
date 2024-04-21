"""A christmas tree!"""
 

__author__ = "730475093"


from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of the program."""
    xmas: Turtle = Turtle()
    xmas.hideturtle
    draw_triangle(xmas, -80, -70, 200)
    draw_square(xmas, -10, -70, 50)
    draw_star(xmas, -9, 235)
    draw_circle(xmas, 8)
    done()


def draw_triangle(leaves: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw 3 equilateral triangles stacked on top of each other and each one is smaller than the one below it."""
    leaves.speed(100)
    leaves.hideturtle
    counter: int = 0
    while counter < 3:
        leaves.begin_fill()
        leaves.pencolor("green")
        leaves.penup()
        leaves.goto(x, y)
        leaves.pendown()
        i: int = 0
        while i < 3:
            leaves.forward(side_length)
            leaves.left(120)
            i += 1
        leaves.color("green")
        leaves.end_fill()
        x += 26
        y += 100
        side_length *= 0.7
        counter += 1


def draw_square(trunk: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    trunk.speed(100)
    trunk.hideturtle
    trunk.begin_fill()
    trunk.penup()
    trunk.goto(x, y)
    trunk.setheading(0.0)
    trunk.pendown()
    i: int = 0
    while i < 4:
        trunk.forward(width)
        trunk.right(90)
        i += 1
    trunk.color("brown")
    trunk.end_fill()


def draw_circle(ornament: Turtle, radius: float) -> None:
    """Draw multiple multi-colored circles in different places around the tree.
    Used random to place ornaments at random coordinates within range of tree AND to randomize the fill and pen color of the ornament using RBG."""
    ornament.speed(200)
    ornament.hideturtle
    counter: int = 0
    while counter < 20:
        ornament.begin_fill()
        ornament.penup()
        ornament.goto(randint(-20, 50), randint(-80, 180))
        ornament.pendown()
        ornament.circle(radius)
        ornament.color(randint(0, 255), randint(0, 255), randint(0, 255))
        ornament.end_fill()
        counter += 1


def draw_star(star: Turtle, x: float, y: float) -> None:
    """Draw a yellow star on top of the tree."""
    star.speed(100)
    star.hideturtle
    star.begin_fill()
    star.pencolor("yellow")
    star.penup()
    star.goto(x, y)
    star.pendown()
    counter: int = 0
    while counter < 5:
        star.forward(60)
        star.right(144)
        counter += 1
    star.color("yellow")
    star.end_fill()
        

if __name__ == "__main__":
    main()