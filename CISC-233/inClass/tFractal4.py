import turtle
import random

def tree(t, branchLen):
    if branchLen > 5:
        one = random.randrange(15,30)
        color = branchLen/10
        t.pensize(color)
        t.pencolor("black")
        if color < 5:
            t.pencolor("green") 
        t.forward(branchLen)
        t.right(one)
        tree(t, branchLen-15)
        t.left(one)
        tree(t, branchLen-15)
        t.right(one)
        t.backward(branchLen)

t = turtle.Turtle()
t.speed(10)
branchLen = 100
tree(t, branchLen)
wait = raw_input("Wait: ")
