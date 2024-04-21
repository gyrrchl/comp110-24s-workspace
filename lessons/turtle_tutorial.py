from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
side_length: int = 20
side_length = side_length * 20

leo.speed(50)
leo.hideturtle()
leo.begin_fill()
leo.pencolor("pink")
leo.penup()
leo.goto(-150, -100)
leo.pendown()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(100)
    i = i + 1
leo.color("pink", "pink")
leo.end_fill()
done()