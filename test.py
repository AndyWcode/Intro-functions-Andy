import turtle
from turtle import *
t = Turtle()


t.shape('turtle')


# Answer for intro.md

def equalsides(x):
    for side in range(3):
        t.forward(x)
        t.left(120)

def rectangle(x, y):
    for side in range(2):
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.left(90)

def square(x):
    for square in range(4):
        
        t.forward(x)
        t.left(90)
        
turtle.done()

