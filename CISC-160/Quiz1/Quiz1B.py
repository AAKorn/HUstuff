import random
n = int(raw_input("What length 'n' would you like your arrays to be?: "))
a = [random.randrange(0,100) for i in xrange(0,n)]
b = [random.randrange(0,100) for i in xrange(0,n)]
c =[a[i]+b[i] for i in xrange(0, n-1)]
print c
