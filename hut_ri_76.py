import turtle
import time

t = turtle.Turtle()
t.fillcolor("#E52B2D")
t.penup()
t.goto(-250,250)

def seven():
    t.begin_fill()
    t.pendown()
    t.fd(300)
    t.right(100)
    t.fd(100)
    t.fd(325)
    t.right(50)
    t.fd(125)
    t.right(130)
    t.fd(325)
    t.right(50)
    t.fd(125)
    t.left(150)
    t.fd(230)
    t.right(60)
    t.fd(115)
    t.right(120)
    t.end_fill()

def space1():
    t.penup()
    t.fd(5)
    t.fd(410)
    t.right(100)
    t.fd(160)
    t.pendown()

def six():
    t.begin_fill()
    t.fd(200)
    t.left(130)
    t.fd(125)
    t.left(50)
    t.fd(80)
    t.left(50)
    t.fd(125)
    t.left(130)
    t.end_fill()

def space2():
    t.penup()
    t.fd(188)
    t.right(15)
    t.fd(100)
    t.pendown()

def circle1():
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def space3():
    t.penup()
    t.left(90)
    t.fd(70)
    t.right(90)
    t.pendown()

def circle2():
    t.fillcolor("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def space4():
    t.penup()
    t.right(90)
    t.fd(70)
    t.right(75)
    t.fd(390)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.pendown()

def T():
    t.fillcolor("#E52B2D")
    t.begin_fill()
    t.right(80)
    t.fd(40)
    t.right(90)
    t.fd(10)
    t.right(90)
    t.fd(15)
    t.left(90)
    t.fd(40)
    t.right(90)
    t.fd(10)
    t.right(90)
    t.fd(40)
    t.left(90)
    t.fd(15)
    t.right(90)
    t.fd(10)
    t.right(90)
    t.end_fill()

def space5():
    t.penup()
    t.fd(50)
    t.pendown()

def H():
    t.begin_fill()
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(8)
    t.left(90)
    t.fd(21)
    t.right(90)
    t.fd(18)
    t.right(90)
    t.fd(21)
    t.left(90)
    t.fd(8)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(8)
    t.left(90)
    t.fd(21)
    t.right(90)
    t.fd(18)
    t.right(90)
    t.fd(21)
    t.left(90)
    t.fd(8)
    t.end_fill()

seven()
space1()
six()
space2()
circle1()
space3()
circle2()
space4()
T()
space5()
H()

time.sleep(100)