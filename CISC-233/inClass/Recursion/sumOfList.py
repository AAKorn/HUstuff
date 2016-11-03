def sumOfList(lisT):
    for x in xrange(0,10):
        lisT.append(x)
        if x == 9:
            print lisT
            print sum(lisT)        

lisT = []
sumOfList(lisT)
