class linkedQueue:
  #Nested Node class
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node
        __slots__='_element'.'_Next'"""

        def __init__(self, element, Next):
            self._element = element
            self._Next = Next

#Constructor for the linkedQueue
    def __init__(self):
        self._head = None
        self._current = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

#Check if the linkedQueue is empty
    def isEmpty(self):
        return self._size == 0

#Return first element in the linkedQueue
    def first(self):
        if self.isEmpty():
            raise Empty("Queue is empty")

        return self._head._element

    def firstObj(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        
        return self._head

    def currentElement(self):
        if self.isEmpty():
            raise Empty("Queue is empty")

        return self._current._element

    def nextCurrent(self):
        if self.isEmpty():
            raise Empty("Queue is empty")

        return self._current._Next

    def last(self):
        if self.isEmpty():
            raise Empty("Queue is empty")

        return self._tail._element

#Enqueue function
    def enqueue(self, element):
        newest = self._Node(element, None)
        if self.isEmpty():
            self._head = newest
        
        else:
            self._tail._Next = newest

        self._tail = newest
        self._size += 1

#Dequeue function
    def dequeue(self):
        if self.isEmpty():
            raise Empty("Queue is empty")

        answer = self._head._element
        self._head = self._head._Next
        self._size -= 1
    
        if self.isEmpty():
            self._tail = None

        return answer

    def secondToLast(self, head):

        if head == "GO": 
            self._current = self._head
        else:
            self._current = head


        if self._current._Next._element == self._tail._element:
            return self._current._element

        newCurrent = self._current._Next

        return self.secondToLast(newCurrent)
    
    def isSorted(self, head):
        
        if head == "GO":
            self._current = self._head
        else:
            self._current = head

        if self._current._Next != None:        

            if self._current._Next._element > self._current._element:
                newCurrent = self._current._Next
                return self.isSorted(newCurrent)
            else:
                return False
        else:
            return True            

    def mergeList(self, l2):

        if self.isEmpty():
            raise Exception("List is empty")
        if l2.isEmpty():
            return "List 2 is empty, therefore no merging is needed"

        if self.isSorted("GO") and l2.isSorted("GO"):
            for x in range(len(l2)):
                
                if x == 0:
                    l2._current = l2._head
                else:
                    l2._current = l2.nextCurrent()
                self.enqueue(l2.currentElement())
            return "Lists Merged"
        else:
            return False
