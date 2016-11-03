def reverseString(string):
    listString = list(string)
    newListString = []
    print listString
    for x in xrange(0,len(listString)):
        newListString.insert(0, listString[x])
        print newListString

string = "Alex"

reverseString(string)
