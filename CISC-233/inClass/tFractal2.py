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
