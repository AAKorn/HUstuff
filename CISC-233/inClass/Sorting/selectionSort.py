import random
def selectionSort(aList):
    for fillSlot in range(len(aList)-1, 0, -1):
        positionOfMax = 0

        for location in range(1, fillSlot + 1):

            if aList[location] > aList[positionOfMax]:
                positionOfMax = location

        temp = aList[fillSlot]
        aList[fillSlot] = aList[positionOfMax]
        aList[positionOfMax] = temp
    
    return aList

aList = [random.randrange(0,10000) for x in range(10000)]
print selectionSort(aList)
