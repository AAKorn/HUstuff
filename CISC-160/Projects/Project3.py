from linkedListQueue import linkedQueue

l1 = linkedQueue()
l2 = linkedQueue()
l1.enqueue(1)
l1.enqueue(2)
l1.enqueue(3)

l2.enqueue(4)
l2.enqueue(5)
l2.enqueue(6)
l2.enqueue(7)

print l1.mergeList(l2)

print l1.last()
