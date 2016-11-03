m = 11
hashTable = [None for x in xrange(m)]

def hashTableFun(name):
    nameList = [] 
    
    global m
    global hashTable

    for x in name:
        if ord(x) != 32:
            nameList.append(ord(x)) 

    slot = sum(nameList) % m
    
    #Collision fixing by finding the next unoccupied slot.
    if hashTable[slot] == None or hashTable[slot] == name:
        hashTable[slot] = name

    else:
        for x in xrange(m):
            if hashTable[x] == None:
                hashTable[x] = name
                break
        
    print hashTable
    
    if None in hashTable:
        hashTableFun(raw_input("What is your name?: "))

hashTableFun(raw_input("What is your name?: "))
