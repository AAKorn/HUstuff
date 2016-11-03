import turtle

def turtleRecursion(self, n):
    if float(n) >= 1:
        self.forward(n)
        self.right(90)
        n = n/float(1.05)
        turtleRecursion(self, n)
    else:
        return


Korn = turtle.Turtle()
n = 100
Korn.speed(8)
turtleRecursion(Korn, n)
