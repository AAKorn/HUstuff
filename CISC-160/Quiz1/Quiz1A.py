import random
lisT = []
for x in xrange(0,10):
    randNum = random.randrange(0,100)
    lisT.append(randNum)
def allDiff(lisT):
    for x in lisT:
        count = 0
        for e in lisT:
            if x == e:
                count+=1
                if count >=2:
                    print x, "is the same as", e
                    return
    print "All numbers are different"
allDiff(lisT)
