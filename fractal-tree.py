#todo
import turtle

t = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor('black')

# move pen to new origin
t.penup()
t.setpos(-150,50) # relative pixel positions
t.pendown()
t.speed(0) # set speed to fast

t.color("orange")

def fractal_tree(t, size):
    t.left(90)
    t.forward(size)
    t.left(45)
    t.forward(size / 2)
    return

fractal_tree(t, 100)
wn.exitonclick()