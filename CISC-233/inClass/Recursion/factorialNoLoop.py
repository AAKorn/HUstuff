def factorial(n):
    if n <= 1:
        return n
    else:
        y =  n * factorial(n-1)
        return y

def lenFactorial(n):

    if type(n) == long:
        newN = list(str(n))
        lenFactorial(newN)

    else:
        print len(n)

x = str(factorial(999))
n = long(x)

print x
lenFactorial(n)
