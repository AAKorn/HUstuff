class Stack:

#Constructor for the Stack class
    def __init__(self, maxlen = None):
        self.items = []
        self._maxlen = maxlen

#Is an override for the built in str function
    def __str__(self):
        return str(self.items)

    def isFull(self):
        return self._maxlen == self.size()

    
#Returns if the stack is empty
    def isEmpty(self):
        return self.items == []

#Places the current item at the end, or top, of the stack.
    def push(self, item):
        if self.isFull() == False:
            self.items.append(item)
        else:
            print "Error, stack is full"
        
#Returns removing the last item in the  stack.
    def pop(self):
        return self.items.pop()

#Returns the last item placed into the stack.  
    def peek(self):
        return self.items[len(self.items) - 1]

#Returns the size of the stack.
    def size(self):
        return len(self.items)

#Reverses the list.
    def reverse(self):
        self.items.reverse()

