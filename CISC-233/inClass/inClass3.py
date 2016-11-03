import random
def printHalf():
    x = [random.randrange(0,100) for i in range(21)]
    print x
    counter = 0
    while len(x) != 1:
        x = [x[i] for i in range(0, len(x) / 2)]
        print x 
        counter +=1
    print counter
printHalf()
