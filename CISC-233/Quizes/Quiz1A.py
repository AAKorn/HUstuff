import random
randomNums=[]
n = 10
for x in xrange(0,10):
    randomNums.append(random.randrange(0,n))

def checkNum(randomNums):
    leastNum = n+1    
    for x in randomNums:
        for e in randomNums:
            if x < e and x < leastNum:
                leastNum = x
    showNum(randomNums, leastNum)

def showNum(randomNums, leastNum):
    print randomNums
    print leastNum

checkNum(randomNums)
