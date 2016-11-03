def orderAndSequenceSearch(alist, request):
    alist.sort()
    print alist
    index = 0
    found = False
    lengthList = len(alist)
    print lengthList
    while index < lengthList and not found :
        if alist[index] == request:
            found = True
        else:
            if alist[index] > request:
                break
            else:
                index = index + 1
    return found

import random
alist = [random.randrange(0,100) for x in xrange(100)]
print orderAndSequenceSearch(alist, 20)
