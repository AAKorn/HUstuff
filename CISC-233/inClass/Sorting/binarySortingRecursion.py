import random
alist = [random.randrange(0,10000) for x in xrange(1000000)]

counter = 0
first = 0
last = len(alist)-1


def binaryRSearch(alist, request):

    global counter
    counter = counter + 1
    global first
    global last

    alist.sort()
    
    midpoint = (first + last)//2

    if counter > 100:
        return False

    if alist[midpoint] == request:
        print alist
        print counter
	return True
    else:
        if request < alist[midpoint]:
            last = midpoint - 1
            return binaryRSearch(alist, request) 
        else:
            first = midpoint + 1
            return binaryRSearch(alist, request)

print binaryRSearch(alist, 5)

