import turtle 
turtle.bgcolor("white")

#FOR FLOWER
def petal(t, r, angle):
    
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

def flower(t, n, r, angle):

    for i in range(n):
        petal(t, r, angle)
        t.left(360.0/n)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

#FOR TREE
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75,t)

def dope_flowers(x, y):
    turtle.pendown()
    turtle.begin_fill()
    move(turtle, 100)
    flower(turtle, 10, 20.0, 60.0)
    turtle.end_fill()
    turtle.penup()
    
main()        #TREE

turtle = turtle.Pen()
turtle.speed(3)

#FLOWERZZZZZ

turtle.color("green")
turtle.penup()
turtle.goto(-10,85)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()

turtle.color("green")
turtle.penup()
turtle.goto(-5,85)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()

turtle.color("green")
turtle.penup()
turtle.goto(-40,100)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()

turtle.color("green")
turtle.penup()
turtle.goto(-35,100)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()

turtle.color("green")
turtle.penup()
turtle.goto(-190,85)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()

turtle.color("green")
turtle.penup()
turtle.goto(-185,85)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()

turtle.color("green")
turtle.penup()
turtle.goto(-130,110)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()

turtle.color("green")
turtle.penup()
turtle.goto(-125,110)
turtle.pendown()
turtle.begin_fill()
move(turtle, 100)
flower(turtle, 10, 20.0, 60.0)
turtle.end_fill()
turtle.penup()
