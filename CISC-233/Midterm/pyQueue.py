class ArrayQueue:

    DEFAULT_CAPACITY = 10

#Construct the ArrayQueue, Array meaning that our Queue will be of fixed size.
    def __init__(self):

        #Create an "empty" list of DEFAULT_CAPACITY size
        self.elements = [None] * ArrayQueue.DEFAULT_CAPACITY

        #Serves as the amount of queued elements in the list
        self.size = 0

        #Serves as the index for our new front of the list
        self.front = 0

#Override the len function to return the size of our ArrayQueue        
    def __len__(self):
        return self.size

#Override the str function to return the str of the elements of our ArrayQueue.
    def __str__(self):
        return str(self.elements)

#Check if the size of our list is 0.
    def isEmpty(self):
        return self.size == 0

#Returns the first element in the queue.
    def first(self):
        if self.isEmpty():
            raise "Queue is empty"
        return self.elements[self.front]

#Place your element into the back of the queue.
    def enqueue(self, e):

        #This is so we do not crash in the event the queue runs out of space 
        if self.size == len(self.elements):
            self.resize(2 * len(self.elements)) #double the array size
        
        #Because the remainder produced will be the next space in the queue. 
        avail = (self.front + self.size) % len(self.elements)

        self.elements[avail] = e
        self.size +=1

#Remove and return the first element of the queue. 
    def dequeue(self):
        #Raise Empty exception if the queue is empty.

        if self.isEmpty():
            raise "Queue is empty"

        answer = self.elements[self.front]

        self.elements[self.front] = None
        #Becuase the remainder will serve as the index for the new front element
        self.front = (self.front + 1) % len(self.elements)
        #The size is now reduced by the element we dequeued
        self.size -=1

        return answer


    def resize(self, cap):
        #Resize to a new list of capacity >= len(self)

        old = self.elements
        self.elements = [None] * cap
        walk = self.front
        
        #Iterate over the size of the old list.
        for k in range(self.size):
            #Place all of the old elements back in there original place.
            self.elements[k] = old[walk]
            #
            walk = (1 + walk) % len(old)
        #Because our new ArrayQueue will begin again at index 0
        self.front = 0
