def isSquare(integer):
    for x in xrange(1,10000000):
        if integer/x == x:
            print integer
            print "This number's perfect square root is " + str(x)
            break
    print integer
    print "This number does not have a perfect square root"

isSquare(3)
