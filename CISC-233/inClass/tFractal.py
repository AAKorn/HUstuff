import turtle

def tree(t, branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(t, branchLen-15)
        t.left(40)
        tree(t, branchLen-15)
        t.right(20)
        t.backward(branchLen)

t = turtle.Turtle()
t.speed(10)
branchLen = 30
tree(t, branchLen)

