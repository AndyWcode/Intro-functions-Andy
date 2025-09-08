import turtle
from turtle import *
t = Turtle()


t.shape('turtle')



def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)

def equalsides(x):
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)

def rectangle():
    t.left(90)
    t.forward()
    


turtle.done()