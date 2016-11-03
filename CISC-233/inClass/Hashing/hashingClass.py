class nestedHashTable:
    
    def __init__(self, length):
        self.elements = [[] for x in xrange(length)]
        self.length = length
    
    def insertElements(self, element):
        slot = self.hashIndex(element) % self.length  
        if element not in self.elements[slot]:
            self.elements[slot].append(element)

    def getElements(self):
        return self.elements

    def findElement(self, element):
        find = self.hashIndex(element)
        slot = find % self.length

        for x in self.elements[slot]:
            if x == find:
                return True 


    def hashIndex(self, element):
        return ord(element)




hash1 = nestedHashTable(11)

print hash1.getElements()

import random
for x in xrange(1000):
    hash1.insertElements(chr(random.randrange(65,91)))
print hash1.getElements()


