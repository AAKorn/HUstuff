class List:

    def __init__(self):
        self.__data = []

    def addObject(self, myObject):
        self.__data.append(myObject)
    
    def removeObject(self, myObject):
        self.__data.pop(myObject)

    def printList(self):
        print self.__data

    def returnList(self):
        return self.__data

    def isEmpty(self):
        return len(self.__data) == 0

YourMom = List()
YourMom.addObject(100)
YourMom.printList()
