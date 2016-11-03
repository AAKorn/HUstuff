import random
x = []
for i in xrange(0,10):
    a = random.randrange(0,10)
    x.append(a)
print x
for i in x:
    print "***************",i,"*****************"
    count = 0
    count2 = 0
    for e in x:
        if i == e:
            count = count + 1
        if e == x[9] and count2 < 1:
            print count
            count2 = count2 + 1
