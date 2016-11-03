def binarySearch(alist, request):
    alist.sort()
    print alist
    first = 0
    counter = 0
    last = len(alist)-1
    found = False
    while first <= last and not found :
        counter = counter + 1
        midpoint = (first + last)//2
        if alist[midpoint] == request:
            found = True
        else:
            if request < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    print counter
    return found

import random
alist = [random.randrange(0,100000) for x in xrange(100000)]
print binarySearch(alist, 20)
