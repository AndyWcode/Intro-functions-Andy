import turtle
from turtle import *
t = Turtle()


t.shape('turtle')


# Answer for intro.md

def equalsides(x):
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)

def rectangle(x, y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)

equalsides(90)
rectangle(125,100)


turtle.done()