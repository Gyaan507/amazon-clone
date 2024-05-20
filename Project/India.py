import turtle


screen = turtle.Screen()
screen.title("Tiranga")
screen.bgcolor("white")

flag_turtle = turtle.Turtle()
flag_turtle.speed(1)


def draw_rectangle(color, width, height):
    flag_turtle.begin_fill()
    flag_turtle.fillcolor(color)
    for _ in range(2):
        flag_turtle.forward(width)
        flag_turtle.right(90)
        flag_turtle.forward(height)
        flag_turtle.right(90)
    flag_turtle.end_fill()


flag_turtle.penup()
flag_turtle.goto(-300, 200)
flag_turtle.pendown()
draw_rectangle("#FF9933", 600, 100)


flag_turtle.penup()
flag_turtle.goto(-300, 100)
flag_turtle.pendown()
draw_rectangle("white", 600, 100)

flag_turtle.penup()
flag_turtle.goto(-300, 0)
flag_turtle.pendown()
draw_rectangle("#138808", 600, 100)


flag_turtle.penup()
flag_turtle.goto(00, 25)
flag_turtle.pendown()
flag_turtle.color("#000080")
flag_turtle.circle(25)


flag_turtle.penup()
flag_turtle.goto(00, 50)
flag_turtle.pendown()
for _ in range(24):
    flag_turtle.forward(25)
    flag_turtle.backward(25)
    flag_turtle.left(15)

flag_turtle.hideturtle()


turtle.done()
