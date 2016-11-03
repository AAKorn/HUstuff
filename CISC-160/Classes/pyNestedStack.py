class nestedStack:

#Constructor for the Stack class
    def __init__(self):
        self.items = []

#Is an override for the built in str function
    def __str__(self):
        return str(self.items)

#Returns if the stack is empty
    def isEmpty(self):
        return self.items == []

#Places the current item at the end, or top, of the stack.
    def push(self, item):
        self.items.append(item)

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

    def join(self, other):
        self.items = other.items + self.items
        return self.items

S = nestedStack()
S.push(4)
S.push(5)

T = Stack()
T.push(6)
T.push(7)
T.push(8)
T.push(9)

print S.join(T)
