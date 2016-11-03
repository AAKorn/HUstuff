##############NUMBER 1####################

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

##############NUMBER 3####################

n = int(raw_input("What is n?: "))
nums = []

if n > 0:
    n2 = (2*n)+1
else:
    print "n must be a positive integer"

for x in xrange(0,n2):
    if x % 2 == 0:
        nums.append(x)
print sum(nums)

##############NUMBER 4####################

s =raw_input("Type your string: ")
for char in ["'",".","!","?"]:
    if char in s:
        s=s.replace(char,"") 
print s
