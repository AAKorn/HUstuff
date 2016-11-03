from pyQueue import ArrayQueue

queue = ArrayQueue()

queue.enqueue(5)
print queue
queue.enqueue(3)
print queue
queue.dequeue()
print queue
queue.enqueue(2)
print queue
queue.enqueue(8)
print queue
queue.dequeue()
print queue
queue.dequeue()
print queue
queue.enqueue(9)
print queue
queue.enqueue(1)
print queue
queue.dequeue()
print queue
queue.enqueue(7)
print queue
queue.enqueue(6)
print queue
queue.dequeue()
print queue
queue.dequeue()
print queue
queue.enqueue(4)
print queue
queue.dequeue()
print queue
queue.dequeue()
print queue
#Code output below
'''
[5, None, None, None, None, None, None, None, None, None]
[5, 3, None, None, None, None, None, None, None, None]
[None, 3, None, None, None, None, None, None, None, None]
[None, 3, 2, None, None, None, None, None, None, None]
[None, 3, 2, 8, None, None, None, None, None, None]
[None, None, 2, 8, None, None, None, None, None, None]
[None, None, None, 8, None, None, None, None, None, None]
[None, None, None, 8, 9, None, None, None, None, None]
[None, None, None, 8, 9, 1, None, None, None, None]
[None, None, None, None, 9, 1, None, None, None, None]
[None, None, None, None, 9, 1, 7, None, None, None]
[None, None, None, None, 9, 1, 7, 6, None, None]
[None, None, None, None, None, 1, 7, 6, None, None]
[None, None, None, None, None, None, 7, 6, None, None]
[None, None, None, None, None, None, 7, 6, 4, None]
[None, None, None, None, None, None, None, 6, 4, None]
[None, None, None, None, None, None, None, None, 4, None]
'''


