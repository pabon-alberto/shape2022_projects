import turtle

t = turtle.Turtle()
t.penup()
t.setpos(-200, 0)
t.pendown()


def koch(t, order = 1, size = 300):

    if order == 0:
        t.forward(size)

    koch(t, order - 1, size // 3)
    t.left(60)
    koch(t, order - 1, size // 3)
    t.right(120)
    koch(t, order - 1, size // 3)
    t.left(60)
    koch(t, order - 1, size // 3)

koch(t, 2, 200)
wn = turtle.Screen()
wn.exitonclick()
turtle.bye()