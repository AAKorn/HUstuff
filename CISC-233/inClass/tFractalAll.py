#Question 1
import turtle

def tree(t, branchLen):
    if branchLen > 5:
        t.pensize(branchLen/10) 
        t.forward(branchLen)
        t.right(20)
        tree(t, branchLen-15)
        t.left(40)
        tree(t, branchLen-15)
        t.right(20)
        t.backward(branchLen)

t = turtle.Turtle()
t.speed(10)
branchLen = 100
tree(t, branchLen)
wait = raw_input("Wait: ")

#Question 2
import turtle

def tree(t, branchLen):
    if branchLen > 5:
        color = branchLen/10
        t.pensize(color)
        t.pencolor("black")
        if color < 5:
            t.pencolor("green") 
        t.forward(branchLen)
        t.right(20)
        tree(t, branchLen-15)
        t.left(40)
        tree(t, branchLen-15)
        t.right(20)
        t.backward(branchLen)

t = turtle.Turtle()
t.speed(10)
branchLen = 100
tree(t, branchLen)
wait = raw_input("Wait: ")

#Question 3
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

#Question 4
import turtle
import random

def tree(t, branchLen):
    if branchLen > 5:
        one = random.randrange(15, 30)
        two = random.randrange(5, 15)
        color = branchLen/10
        t.pensize(color)
        t.pencolor("black")
        if color < 5:
            t.pencolor("green") 
        t.forward(branchLen)
        t.right(one)
        tree(t, branchLen-two)
        t.left(one)
        tree(t, branchLen-two)
        t.right(one)
        t.backward(branchLen)

t = turtle.Turtle()
t.speed(10)
branchLen = 100
tree(t, branchLen)
wait = raw_input("Wait: ")
