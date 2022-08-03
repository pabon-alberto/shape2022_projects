from itertools import starmap
import turtle

t = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor('black')

# move pen to new origin
t.penup()
t.setpos(-150,50) # relative pixel positions
t.pendown()
t.speed(1) # set speed to fast

t.color("orange")

def square(t, size): 
    for i in range(4):
        t.forward(size)
        t.left(90)
    return

def triangle(t, size):
    for i in range(3):
        t.forward(size)
        t.left(120)
    return

def star(t, size):
    for i in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)
    return

def star_with_interior_angles(t, size):
    for i in range(6):
        t.forward(size)
        t.right(216)


def n_pointed_star(t, size): #todo
    for i in range(5):
        t.forward(size)
        t.right(216)
    return

def sierpinski_triangle(t, size, n):
    big = False
    if big != True:    
        for i in range(3):
            t.forward(size)
            t.right(120)

    big = True

    if big == True:
        for i in range(3):
            size = size / 2
            t.forward(size)
            t.right(120)
            t.forward(size)
    

    

    # for x in range(1):
    #     sierpinski_triangle(t, (size / 2), 0)
    return

big = False
sierpinski_triangle(t, 100, 3)
wn.exitonclick()